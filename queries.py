from db_connection import connection
from db_connection import cursor

def select_all(table):
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()

    for data in result:
        print(data)
