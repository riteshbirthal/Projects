import snowflake
import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
from config import *


def sf_connection():
    conn = snowflake.connector.connect(
        user = connection_parameters["user"],
        password = connection_parameters["password"],
        account = connection_parameters["account"],
        database = connection_parameters["database"],
        schema = connection_parameters["schema"],
        warehouse = connection_parameters["warehouse"],
        role = connection_parameters["role"]
    )
    cursor_sf = conn.cursor()
    return conn, cursor_sf


def update_data(conn, cursor_sf, results, table_name):
    for idx, row in results.iterrows():
        try:
            cursor_sf.execute(f"""UPDATE {table_name} SET COLA = 'TRUE' WHERE COLB = {row['COLB']};""")
        except:
            return False
    conn.commit()
    return True


# check will be True and table name will be given in case when reading the table which should contain COLA data else table_name will be empty string and check will be False
def sf_data(conn, cursor_sf, query, table_name, check):
    try:
        if check:
            try:
                cursor_sf.execute(f"SELECT COLA FROM {table_name}")
                flag = False
            except:
                flag = True
            if flag:
                cursor_sf.execute(f"""ALTER TABLE {table_name} ADD COLUMN COLA VARCHAR""")
                print("COLA Column added")
                conn.commit()
        cursor_sf.execute(query)
        data = cursor_sf.fetchall()
        df = pd.DataFrame(data, columns=[x[0] for x in cursor_sf.description])
        if check:
            df = df[df["COLA"]!="TRUE"]
        return {"Success" : True, "data" : df}
    except:
        print("error occured...")
        return {"Success": False, "data" : []}
    

# main function data.....

query1 = open("test_query1.sql", "r").read()
query2 = open("test_query2.sql", "r").read()


conn, cursor_sf = sf_connection()

sf_data0 = sf_data(conn, cursor_sf, query1, "", False)
sf_data1 = sf_data(conn, cursor_sf, query2, "TESTING_DATABASE.PUBLIC.TABLE_NAME1", True)
print("SF DATA0: ", sf_data0)
print("\n\n SF DATA1: ", sf_data1)


sf_data_final = pd.merge(sf_data0["data"], sf_data1["data"], on="COLB")

# update the data to snowflake table
update_data(conn, cursor_sf, sf_data_final, "TESTING_DATABASE.PUBLIC.TABLE_NAME1")

sf_data2 = sf_data(conn, cursor_sf, query2, "", False)

print("\n\n SF_DATA: ", sf_data2["data"])
