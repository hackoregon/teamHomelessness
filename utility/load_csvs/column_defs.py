def col_dtype_dict():
    """
    return a dict that maps col names to correct data type 
    """
    dtype_dict = {
        "shelterType": "VARCHAR(255) NOT NULL",
        "age": "VARCHAR(255) NOT NULL",
        "propYes": "DOUBLE PRECISION", 
        "propNo": "DOUBLE PRECISION",
        "countYes": "INTEGER",
        "countNo": "INTEGER",
        "yearInPIT": "INTEGER",
        "year": "INTEGER",
        "pageInPIT": "INTEGER",
        "yearPageInPIT": "INTEGER",
        "householdType": "VARCHAR(255) NOT NULL",
        "ethnicity": "VARCHAR(255)",
        "veteran": "VARCHAR(255)",
        "multnomahGeneralAdultPopPercVeterans": "DOUBLE PRECISION",
        "multnomahAdultPopColorPercVeterans": "DOUBLE PRECISION",
        "chronicHomelessPercVeterans": "DOUBLE PRECISION",
        "Gender": "VARCHAR(255) NOT NULL",
        "ageRange": "VARCHAR(255)",
        "geographicLocation": "VARCHAR(255) NOT NULL",
        "count_geographicLoc": "INTEGER",
        "prop_geographicLoc": "DOUBLE PRECISION",
        "total_used_in_calculations": "INTEGER"
    }

    return dtype_dict