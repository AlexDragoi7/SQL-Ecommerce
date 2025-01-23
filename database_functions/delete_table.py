from db_connection import connection
from db_connection import cursor

def delete_table(table):
    drop_table = f'''DROP TABLE {table}'''
    cursor.execute(drop_table)
    connection.commit()
    print(f'Table {table} was deleted')