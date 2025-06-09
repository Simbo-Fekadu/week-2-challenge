import pandas as pd
import oracledb
from datetime import datetime

# Database connection parameters
username = "SYSTEM"
password = "ih3ba3so"
dsn = "10.240.71.131:1521/XE"  # Adjust if service name differs (e.g., orcl)

# Load cleaned data
try:
    df = pd.read_csv('analyzed_reviews.csv')
except FileNotFoundError:
    print("Error: analyzed_reviews.csv not found. Check Task 2 output.")
    exit()

# Connect to Oracle
try:
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()
    print("Connected to Oracle database")
except oracledb.Error as e:
    print(f"Error connecting to Oracle: {e}")
    exit()

# Get bank IDs
bank_ids = {}
cursor.execute("SELECT bank_name, bank_id FROM banks")
for row in cursor:
    bank_ids[row[0]] = row[1]

# Prepare insert statement for reviews
insert_sql = """
INSERT INTO reviews (bank_id, review_text, rating, review_date, source, sentiment_label, sentiment_score, identified_theme)
VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
"""

# Insert reviews
inserted = 0
for index, row in df.iterrows():
    try:
        bank_id = bank_ids.get(row['bank'])
        if bank_id is None:
            print(f"Warning: No bank_id for {row['bank']}, skipping")
            continue
        review_date = datetime.strptime(row['date'], '%Y-%m-%d') if pd.notna(row['date']) else None
        cursor.execute(insert_sql, (
            bank_id,
            row['review'],
            row['rating'],
            review_date,
            row['source'],
            row.get('sentiment_label', None),
            row.get('sentiment_score', None),
            row.get('identified_theme', None)
        ))
        inserted += 1
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

# Commit changes
connection.commit()
print(f"Inserted {inserted} reviews into the database")

# Close connection
cursor.close()
connection.close()