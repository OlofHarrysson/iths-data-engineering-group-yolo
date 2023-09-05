import json

import psycopg2

# read JSON data from file
with open("data.json") as f:
    data = json.load(f)

# connect to the database
conn = psycopg2.connect(host="localhost", database="mydb", user="user", password="pass")

# create a cursor
cur = conn.cursor()

# execute the INSERT statement
cur.execute(
    "INSERT INTO table_name (name, email, city) VALUES (%s, %s, %s)",
    (data["name"], data["email"], data["city"]),
)

# commit the changes to the database
conn.commit()

# close the cursor and connection
cur.close()
conn.close()
