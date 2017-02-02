# Instructions for using db_load_csv.py

This script can load a csv file into a targeted database from the command line.

## Example usage
  ```python db_load_csv.py <target_db> <name_of_csv>```
  - target_db: either 'AWS' or 'local'
  - name_of_csv: csv must be in same directory as db_load_csv.py
  
```python db_load_csv.py AWS Example.csv```--> creates table Example and loads it's data to the AWS database

## Setup for column names and data types   
The dictionary in column_defs.py must also have the name and PostgreSQL data type of the headers (columns) in the csv. If running this for the first time on a new column not in the dictionary you will get a key error. If this happens just add the column name and PostgreSQL data type to the dictionary in the column_defs.py [col_dtype_dict function](https://github.com/hackoregon/teamHomelessness/blob/master/utility/load_csvs/column_defs.py). 

## Setup for project_config.py file
The script needs to have a project_config.py file setup in the same directory that the db_load_csv.py file is in. The project_config.py file has needs two dictionaries in the same format seen below. This is done to avoid commiting passwords to GitHub please don't commit your project_config file. 

```python
AWS = {
    'NAME': 'db_name',
    'HOST': 'host_ip',
    'PORT': '5432',
    'USER': 'user_name',
    'PASSWORD': 'postgres_password'
    }

LOCAL = {
    'NAME': 'db_name',
    'HOST': 'host_ip',
    'PORT': '5432',
    'USER': 'user_name',
    'PASSWORD': 'postgres_password'
    }

```
 

