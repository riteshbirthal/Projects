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
            cursor_sf.execute(f"""UPDATE {table_name} SET COLY = 'TRUE' WHERE COLX = {row['COLX']};""")
        except:
            return False
    conn.commit()
    return True



# check will be True and table name will be given in case when reading the table which should contain SENT_MAIL data else table_name will be empty string and check will be False
def sf_data(cursor_sf, query, table_name, check):
    try:
        if check:
            try:
                cursor_sf.execute(f"SELECT COLY FROM {table_name}")
                flag = False
            except:
                flag = True
            if flag:
                cursor_sf.execute(f"""ALTER TABLE {table_name} ADD COLUMN COLY VARCHAR""")
                print("COLY Column added")
                conn.commit()
        cursor_sf.execute(query)
        data = cursor_sf.fetchall()
        df = pd.DataFrame(data, columns=[x[0] for x in cursor_sf.description])
        if check:
            df = df[df["COLY"]!="TRUE"]
        return df
    except:
        print("error occured...")
        return []


query0 = "SELECT * FROM TESTING_DATABASE.PUBLIC.TABLE_NAME"
query1 = "SELECT * FROM TESTING_DATABASE.PUBLIC.TABLE_NAME"
query2 = "SELECT * FROM TESTING_DATABASE.PUBLIC.TABLE_NAME"


conn, cursor_sf = sf_connection()

sf_data0 = sf_data(cursor_sf, query0, "", False)
sf_data1 = sf_data(cursor_sf, query1, "TESTING_DATABASE.PUBLIC.TABLE_NAME", True)
print("SF DATA0: ", sf_data0)
print("\n\n SF DATA1: ", sf_data1)

sf_data2 = sf_data(cursor_sf, query2, "", False)
sf_data1_columns = sf_data2.columns

# print(sf_data1_columns)
insert_query = """INSERT INTO TESTING_DATABASE.PUBLIC.TABLE_NAME (COL1, COL2, COL3, COL4, COL5, COL6, COL7) 
                                                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""  # has to put %s by number of columns times
# print(insert_query)


sf_data_final = pd.merge(sf_data0, sf_data1, on="COLX")

# update the data to snowflake table
update_data(conn, cursor_sf, sf_data_final, "TESTING_DATABASE.PUBLIC.TABLE_NAME")

sf_data2 = sf_data(cursor_sf, query2, "", False)

print("\n\n SF_DATA: ", sf_data2)
