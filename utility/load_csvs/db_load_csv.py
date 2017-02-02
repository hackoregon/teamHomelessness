import sys
import csv 
import re 
import psycopg2

# you need to make your own local project_config with DB connect info
from project_config import AWS, LOCAL
from column_defs import col_dtype_dict


def connect_to_db(target_db):
    """
    connect to DB and return cursor and conn obj used to make queries 
    pass in the target DB as a command line arg after script name 
    AWS = remote AWS instance, local = local DB 
    """
    if target_db == "AWS":
        info = AWS
    elif target_db == "local":
        info = LOCAL
    else: 
        raise ValueError("invalid DB setup CLI arg use 'AWS' or 'local' ")

    try:
        conn = psycopg2.connect(dbname=info["NAME"], user=info["USER"], 
            host=info["HOST"], password=info["PASSWORD"])
        print("connected to DB")
    except:
        print("I am unable to connect to the database")

    cursor = conn.cursor()

    return cursor, conn


def csv_loader(csv_path):
    """
    loads csv file and extracts headers and table_name from file path
    table name should be the same as the csv file 
    """
    with open(csv_path, "r") as csv_file:
        # reads the first line of csv that contains headers
        headers = csv_file.readline()

        # pulls out table name from csv file path 
        table_name_regex = re.compile(r"([a-z])+(?=\.csv$)", re.IGNORECASE)
        table_match = table_name_regex.search(csv_path)

        try:
            table_name = table_match.group(0) 
        except: 
            raise ValueError("regex failed in table name extract")

        return headers, table_name


def drop_table(table_name):
    """
    create drop table command used in case table is already present
    """
    return "DROP TABLE IF EXISTS {};".format(table_name)


def create_table(table_name, csv_headers):
    """
    take table name, csv header and convert into sql to make table  
    """
    # make dict of col data types 
    dtype_dict = col_dtype_dict()

    # split column headers and format strings with corrent dtype for sql 
    col_headers = csv_headers.strip().split(",")
    column_names = ["{} {}".format(col, dtype_dict[col]) for col in col_headers]
    sql_c_names = ", ".join(column_names)

    create_table_command = """
        CREATE TABLE {t_name} (
                {c_names}
            );
        """
    sql_command = create_table_command.format(t_name=table_name, c_names=sql_c_names)

    return sql_command


def load_data_into_table(csv_path, headers, table_name, cursor):
    """
    write each row to table in DB, wrap every string value in quotes for SQL 
    """
    with open(csv_path, "r") as csv_file:
        # need to skip line with headers 
        csv_file.next()
        
        for line in csv_file:  
            # ----------------------------------------------------
            # need to wrap any string values in quotes to avoid SQL error 
            line_split = line.split(",")
            new_line = []
            pattern = r'([a-z])\w+'

            for item in line_split:

                if re.match(pattern, item, re.IGNORECASE):
                    new_line.append("'{}'".format(item))
                elif item == '':
                    new_line.append("NULL")
                else:  
                    new_line.append(item)

            new_line = ','.join(new_line)
            # ----------------------------------------------------

            sql = "INSERT INTO {} ({}) VALUES ({});".format(table_name, headers, new_line)

            cursor.execute(sql)

    return

       
def interface(target_db, csv_path):
    """
    takes a csv file and creates a table in the specified DB using the 
    headers for column names and the csv's file name as the table name
    """
    # connect to DB and grab cursor and connection objects
    cursor, conn = connect_to_db(target_db)

    # extract headers and table names 
    headers, table_name = csv_loader(csv_path)

    # drop table if an old one is present 
    drop_command = drop_table(table_name)
    cursor.execute(drop_command)

    # create new table 
    create_command = create_table(table_name, headers)
    cursor.execute(create_command)
    conn.commit()

    # transform and load rows 
    load_data_into_table(csv_path, headers, table_name, cursor)
    conn.commit()
    
    cursor.close()

    print("table and data in DB")

    return 


def cli_interface():
    """
    wrapper_cli method that interfaces from commandline to function space
    call the script with: 
    python db_load_csvs.py <target_db: 'AWS' or 'local'> <path to csv> 

    """
    try:
        # grabs csv file path and target DB passed in as command line arg
        target_db = sys.argv[1]
        csv_path = sys.argv[2]

    except:
        print("usage: {} <target_db: AWS, local> <csv_file_path>".format(sys.argv[0]))
        sys.exit(1)
    interface(target_db, csv_path)


if __name__ == "__main__":
    cli_interface()