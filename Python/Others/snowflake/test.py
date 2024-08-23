import snowflake
import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
from config import *
from sqlalchemy import create_engine


query0 = "SQL QUERY 1"

query1 = "SQL QUERY 2"

query2 = "SQL QUERY 3"


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

def update_data(conn, cursor_sf, COLB_COLH, results_sf):
    results_sf.loc["COLA", results_sf['COLB'].isin(COLB_COLH)] = "True"
    # cursor_sf.execute()
    # df.to_sql('tablename', con=conn , index= False, if_exists='append')
    success, nchunks, nrows, _ = write_pandas(conn, results_sf, "table_name")


def update_data2(conn, results_sf, table_name):
    success, nchunks, nrows, _ = write_pandas(conn, results_sf, table_name=table_name, database="TESTING_DATABASE", schema="PUBLIC")


def sf_data(cursor_sf, query):
    try:
        cursor_sf.execute(query)
        data = cursor_sf.fetchall()
        df = pd.DataFrame(data, columns=[x[0] for x in cursor_sf.description])
        # df = df[df["COLA"]=="False"]
        return df
    except:
        print("error occured...")
        return []


conn, cursor_sf = sf_connection()
# cursor_sf.execute("SELECT current_version()")
# print(cursor_sf.fetchone()[0])
# print(cursor_sf.execute("SELECT * FROM TESTING_DATABASE.PUBLIC.TESTING_TABLE").fetchall())
sf_data1 = sf_data(cursor_sf, "SELECT * FROM TESTING_DATABASE.PUBLIC.TABLE_NAME1")
sf_data2 = sf_data(cursor_sf, "SELECT COLC, COLD, COLE, COLF, COLB, COLG FROM TESTING_DATABASE.PUBLIC.TABLE_NAME2")
print("SF_DATA1: ", sf_data1, "\n\n\n")
print("SF_DATA2: ", sf_data2, "\n\n\n")

sf_data_final = pd.merge(sf_data1, sf_data2, on="COLB")


print("SF_FINAL_DATA: ", sf_data_final, "\n\n\n")

COLB_lst = []
for idx, row in sf_data_final.iterrows():
    COLB_lst.append(row['COLB'])
# sf_data2["COLG"] = "NONE"
sf_data2 = sf_data2.astype({"COLB": int, "COLD": int, "COLG": str})
temp_data = sf_data2.copy()


for ele in COLB_lst:
    temp_data.loc[temp_data["COLB"]==ele, "COLG"] = "FALSE"

# temp_data.loc["COLG", temp_data['COLB'].isin(COLB_lst)] = "True"

print("\n\n\n", temp_data, "\n\n\n")

# update_data2(conn, temp_data, "TABLE_NAME2")


# print(temp_data.values.tolist())

sf_data_temp = sf_data(cursor_sf, "SELECT * FROM TESTING_DATABASE.PUBLIC.TABLE_NAME2")

# print(sf_data_temp.columns)


# cursor_sf.execute("DROP TABLE IF EXISTS TESTING_DATABASE.PUBLIC.TABLE_NAME2")
# conn.commit()
# temp_data = sf_data1


# cursor_sf.execute("CREATE TABLE TESTING_DATABASE.PUBLIC.TABLE_NAME2(COLC VARCHAR, COLD INT)")
# temp_data = pd.DataFrame([], columns = ["COLC", "COLD"])
# temp_data["COLC"] = ["abc", "def"]
# temp_data["COLD"] = [1234, 5678]
# temp_data.to_sql("TESTING_DATABASE.PUBLIC.TABLE_NAME2", conn, if_exists="replace", index=False)


cursor_sf.execute(""" DELETE FROM TESTING_DATABASE.PUBLIC.TABLE_NAME2 """)

cursor_sf.execute("SELECT COLH FROM TESTING_DATABASE.PUBLIC.TABLE_NAME2")
result = cursor_sf.fetchall()
if result==None:
    cursor_sf.execute("""ALTER TABLE TESTING_DATABASE.PUBLIC.TABLE_NAME2 ADD COLUMN COLH VARCHAR""")


temp_data["COLH"] = "NONE"
temp_data["COLH2"] = "TEMP"
for idx, row in temp_data.iterrows():
    print(row.values.tolist())
    cursor_sf.execute("""INSERT INTO TESTING_DATABASE.PUBLIC.TABLE_NAME2 
                    (COLC, COLD, COLE, COLF, COLB, COLG, COLH, COLH2)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, row.values.tolist())

# for idx, row in temp_data.iterrows():
#     cursor_sf.execute(f""" UPDATE TESTING_DATABASE.PUBLIC.TABLE_NAME21 
#                         SET 
#                         COLC = {row["COLC"]}, COLD = {row["COLD"]}, COLE = {row["COLE"]}, COLF = {row["COLF"]}, 
#                         COLB = {row["COLB"]}, COLG = {row["COLG"]};
#                   """)
#     conn.commit()

# cursor_sf.execute(f""" UPDATE TESTING_DATABASE.PUBLIC.TABLE_NAME21 
#                         SET 
#                         COLC = {temp_data["COLC"]}, COLD = {temp_data["COLD"]}, COLE = {temp_data["COLE"]}, COLF = {temp_data["COLF"]}, 
#                         COLB = {temp_data["COLB"]}, COLG = {temp_data["COLG"]};
#                   """)
conn.commit()


# connection_string = f"snowflake://{connection_parameters['user']}:{connection_parameters['password']}@{connection_parameters['account']}/{connection_parameters['database']}/{connection_parameters['warehouse']}/{connection_parameters['role']}"

# engine = create_engine(connection_string)

# temp_data.to_sql("temp_table", engine, if_exists="replace", index=False)
try:
    cursor_sf.execute("SELECT COLH2 FROM TESTING_DATABASE.PUBLIC.TABLE_NAME2")
    print("hello world")
except:
    print("error occured")

result = cursor_sf.fetchall()
print(result)
if result==None or len(result)==0:
    cursor_sf.execute("""ALTER TABLE TESTING_DATABASE.PUBLIC.TABLE_NAME2 ADD COLUMN COLH2 VARCHAR""")

sf_data2 = sf_data(cursor_sf, "SELECT * FROM TESTING_DATABASE.PUBLIC.TABLE_NAME2")
print("SF_DATA2: ", sf_data2)

