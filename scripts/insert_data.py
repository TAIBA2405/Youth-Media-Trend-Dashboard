import pandas as pd
import psycopg2

# Load the CSV file
df = pd.read_csv("data/netflix_titles.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="media_db",
    user="postgres",
    password="taiba2405"
)
cur = conn.cursor()

# Create table (if not exists)
cur.execute("""
    CREATE TABLE IF NOT EXISTS youth_media (
        id SERIAL PRIMARY KEY,
        show_id TEXT,
        type TEXT,
        title TEXT,
        director TEXT,
        "cast" TEXT,
        country TEXT,
        date_added TEXT,
        
        release_year INT,
        rating TEXT,
        duration TEXT,
        listed_in TEXT,
        description TEXT
    )
""")

# Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO youth_media (show_id, type, title, director, "cast", country, date_added, release_year, rating, duration, listed_in, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['show_id'],
        row['type'],
        row['title'],
        row['director'],
        row['cast'],
        row['country'],
        row['date_added'],
        row['release_year'],
        row['rating'],
        row['duration'],
        row['listed_in'],
        row['description']
    ))

conn.commit()
cur.close()
conn.close()
print("Data inserted successfully into PostgreSQL!")
