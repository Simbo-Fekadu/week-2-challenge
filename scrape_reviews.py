from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime

# Define app IDs (replace with actual IDs from Google Play Store)
app_ids = {
    "CBE": "com.combanketh.mobilebanking",  # Replace with actual CBE app ID
    "BOA": "com.boa.boaMobileBanking",  # Replace with actual BOA app ID
    "Dashen": "com.cr2.amolelight"  # Replace with actual Dashen app ID
}

# Scrape reviews
all_reviews = []
for bank, app_id in app_ids.items():
    try:
        result, _ = reviews(
            app_id,
            lang='en',  # Language: English
            country='et',  # Country: Ethiopia
            sort=Sort.NEWEST,  # Sort by newest
            count=400  # Target 400 reviews per bank
        )
        for review in result:
            all_reviews.append({
                'review': review['content'],
                'rating': review['score'],
                'date': review['at'],
                'bank': bank,
                'source': 'Google Play'
            })
        print(f"Scraped {len(result)} reviews for {bank}")
    except Exception as e:
        print(f"Error scraping {bank}: {e}")

# Create DataFrame
df = pd.DataFrame(all_reviews)

# Preprocessing
# Remove duplicates
df = df.drop_duplicates(subset=['review', 'date'])

# Handle missing data
df = df.dropna(subset=['review'])  # Drop rows with missing review text

# Normalize dates to YYYY-MM-DD
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Save to CSV
df.to_csv('bank_reviews.csv', index=False, columns=['review', 'rating', 'date', 'bank', 'source'])

print(f"Collected {len(df)} reviews. Saved to bank_reviews.csv")