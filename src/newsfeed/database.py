import json

import psycopg2

# read JSON data from file
data = "data/data_warehouse/mit/summaries/A_better_way_to_study_ocean_currents.json"
with open(data) as f:
    data = json.load(f)

# connect to the database
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="GAIS1894")

# create a cursor used to excute the commits
cur = conn.cursor()

# execute the INSERT statement
cur.execute(
    "INSERT INTO table_name (uninque_id, title, text, simple, link, published) VALUES (%s, %s, %s, %s, %s, %s)",
    (
        data["unique_id"],
        data["title"],
        data["text"],
        data["simple"],
        data["link"],
        data["published"],
    ),
)

# commit the changes to the database
conn.commit()

# close the cursor and connection
cur.close()
conn.close()
