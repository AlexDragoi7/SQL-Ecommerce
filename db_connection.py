import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg.connect(dbname=os.getenv('DB_NAME'),
                             user=os.getenv('DB_USER'),
                             password=os.getenv('DB_PASSWORD'),
                             host=os.getenv('DB_HOST'),
                             port=os.getenv('DB_PORT'))

if connection:
    print(f"Connected to {os.getenv('DB_NAME')} database")

cursor = connection.cursor()