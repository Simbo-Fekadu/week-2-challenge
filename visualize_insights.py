import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import oracledb
from datetime import datetime

# Database connection (adjust if needed)
username = "SYSTEM"
password = "ih3ba3so"
dsn = "10.240.71.131:1521/XE"

# Fallback: Use CSV if database connection fails
try:
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()
    print("Connected to Oracle database")
    
    # Average rating per bank
    cursor.execute("""
        SELECT b.bank_name, ROUND(AVG(r.rating), 2) AS avg_rating
        FROM banks b
        LEFT JOIN reviews r ON b.bank_id = r.bank_id
        GROUP BY b.bank_name
    """)
    avg_ratings = pd.DataFrame(cursor.fetchall(), columns=['bank_name', 'avg_rating'])

    # Sentiment distribution
    cursor.execute("""
        SELECT b.bank_name, r.sentiment_label, COUNT(*) AS sentiment_count
        FROM banks b
        LEFT JOIN reviews r ON b.bank_id = r.bank_id
        WHERE r.sentiment_label IS NOT NULL
        GROUP BY b.bank_name, r.sentiment_label
    """)
    sentiment_data = pd.DataFrame(cursor.fetchall(), columns=['bank_name', 'sentiment_label', 'sentiment_count'])

    # Top 5 themes
    cursor.execute("""
        SELECT identified_theme, COUNT(*) AS theme_count
        FROM reviews
        WHERE identified_theme IS NOT NULL
        GROUP BY identified_theme
        ORDER BY theme_count DESC
        FETCH FIRST 5 ROWS ONLY
    """)
    themes_data = pd.DataFrame(cursor.fetchall(), columns=['identified_theme', 'theme_count'])

    # Reviews by month
    cursor.execute("""
        SELECT TO_CHAR(review_date, 'YYYY-MM') AS review_month, COUNT(*) AS review_count
        FROM reviews
        WHERE review_date IS NOT NULL
        GROUP BY TO_CHAR(review_date, 'YYYY-MM')
        ORDER BY review_month
    """)
    reviews_by_month = pd.DataFrame(cursor.fetchall(), columns=['review_month', 'review_count'])

    cursor.close()
    connection.close()
except oracledb.Error as e:
    print(f"Error connecting to Oracle: {e}. Using analyzed_reviews.csv instead.")
    df = pd.read_csv('analyzed_reviews.csv')
    
    # Average rating per bank
    avg_ratings = df.groupby('bank')['rating'].mean().reset_index().round(2)
    avg_ratings.columns = ['bank_name', 'avg_rating']

    # Sentiment distribution
    sentiment_data = df.groupby(['bank', 'sentiment_label']).size().reset_index(name='sentiment_count')
    sentiment_data.columns = ['bank_name', 'sentiment_label', 'sentiment_count']

    # Top 5 themes
    themes_data = df['identified_theme'].value_counts().head(5).reset_index()
    themes_data.columns = ['identified_theme', 'theme_count']

    # Reviews by month
    df['review_month'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)
    reviews_by_month = df.groupby('review_month').size().reset_index(name='review_count')

# Set style
sns.set_style("whitegrid")

# 1. Bar chart: Average rating by bank
plt.figure(figsize=(10, 6))
sns.barplot(x='bank_name', y='avg_rating', data=avg_ratings, palette='Blues_d')
plt.title('Average Rating by Bank')
plt.xlabel('Bank')
plt.ylabel('Average Rating')
plt.savefig('avg_rating_by_bank.png')
plt.close()

# 2. Pie chart: Sentiment distribution (all banks)
sentiment_totals = sentiment_data.groupby('sentiment_label')['sentiment_count'].sum()
plt.figure(figsize=(8, 8))
plt.pie(sentiment_totals, labels=sentiment_totals.index, autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('Sentiment Distribution Across All Banks')
plt.savefig('sentiment_distribution.png')
plt.close()

# 3. Bar chart: Top 5 themes
plt.figure(figsize=(10, 6))
sns.barplot(x='theme_count', y='identified_theme', data=themes_data, palette='Greens_d')
plt.title('Top 5 Themes in Reviews')
plt.xlabel('Count')
plt.ylabel('Theme')
plt.savefig('top_themes.png')
plt.close()

# 4. Line chart: Reviews by month
plt.figure(figsize=(12, 6))
sns.lineplot(x='review_month', y='review_count', data=reviews_by_month, marker='o')
plt.title('Number of Reviews by Month')
plt.xlabel('Month')
plt.ylabel('Review Count')
plt.xticks(rotation=45)
plt.savefig('reviews_by_month.png')
plt.close()

print("Visualizations saved: avg_rating_by_bank.png, sentiment_distribution.png, top_themes.png, reviews_by_month.png")