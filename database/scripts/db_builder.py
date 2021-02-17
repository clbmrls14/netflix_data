import csv
import psycopg2

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='netflix' port ='5000'")
cur = conn.cursor()

with open('netflix_titles.csv', 'r', encoding='UTF8') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        cur.execute(
            "INSERT INTO netflix_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

# cur.execute("""
#     CREATE TABLE netflix_data(
#     show_id text PRIMARY KEY,
#     type text,
#     title text,
#     director text,
#     starring text,
#     country text,
#     date_added date,
#     release_year int,
#     rating text,
#     duration text,
#     listed_in text,
#     description text
# )
# """)

conn.commit()


# cur.execute('SELECT * FROM vgsales')
# one_record = cur.fetchone()
# all_records = cur.fetchall()