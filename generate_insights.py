import pandas as pd
import oracledb

# Database connection
username = "SYSTEM"
password = "ih3ba3so"
dsn = "10.240.71.131:1521/XE"

try:
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()
    
    # Average ratings
    cursor.execute("SELECT b.bank_name, ROUND(AVG(r.rating), 2) AS avg_rating FROM banks b LEFT JOIN reviews r ON b.bank_id = r.bank_id GROUP BY b.bank_name")
    avg_ratings = cursor.fetchall()

    # Sentiment distribution
    cursor.execute("SELECT b.bank_name, r.sentiment_label, COUNT(*) AS sentiment_count FROM banks b LEFT JOIN reviews r ON b.bank_id = r.bank_id WHERE r.sentiment_label IS NOT NULL GROUP BY b.bank_name, r.sentiment_label")
    sentiment_data = cursor.fetchall()

    # Top themes
    cursor.execute("SELECT identified_theme, COUNT(*) AS theme_count FROM reviews WHERE identified_theme IS NOT NULL GROUP BY identified_theme ORDER BY theme_count DESC FETCH FIRST 5 ROWS ONLY")
    themes_data = cursor.fetchall()

    cursor.close()
    connection.close()
except oracledb.Error:
    df = pd.read_csv('analyzed_reviews.csv')
    avg_ratings = df.groupby('bank')['rating'].mean().round(2).reset_index().values.tolist()
    sentiment_data = df.groupby(['bank', 'sentiment_label']).size().reset_index(name='sentiment_count').values.tolist()
    themes_data = df['identified_theme'].value_counts().head(5).reset_index().values.tolist()

# Write report
with open('insights_report.md', 'w') as f:
    f.write("# Task 4: Insights and Visualizations\n\n")
    f.write("## Insights\n")
    f.write("### 1. Average Rating by Bank\n")
    for bank, rating in avg_ratings:
        f.write(f"- {bank}: {rating}\n")
    f.write("\n### 2. Sentiment Distribution\n")
    for bank, sentiment, count in sentiment_data:
        f.write(f"- {bank} ({sentiment}): {count} reviews\n")
    f.write("\n### 3. Top 5 Themes\n")
    for theme, count in themes_data:
        f.write(f"- {theme}: {count} reviews\n")
    f.write("\n## Visualizations\n")
    f.write("- Average Rating by Bank: ![Bar Chart](avg_rating_by_bank.png)\n")
    f.write("- Sentiment Distribution: ![Pie Chart](sentiment_distribution.png)\n")
    f.write("- Top 5 Themes: ![Bar Chart](top_themes.png)\n")
    f.write("- Reviews by Month: ![Line Chart](reviews_by_month.png)\n")

print("Insights report saved as insights_report.md")