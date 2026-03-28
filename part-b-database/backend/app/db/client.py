import os
import psycopg

from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT") 

# Connect to PostgreSQL
conn = psycopg.connect(
    host=host,
    dbname=dbname,
    user=user,
    password=password,
    port=port  # default PostgreSQL port
)

print("Connected to PostgreSQL")
# with conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     print(users)



def execute_query(query: str, params: tuple = ()):
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()
        if cursor.description is not None:
            return cursor.fetchall()
        return None


