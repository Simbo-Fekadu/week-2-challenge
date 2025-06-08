import pandas as pd
from textblob import TextBlob
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load the cleaned reviews from Task 1
try:
    df = pd.read_csv('bank_reviews.csv')
except FileNotFoundError:
    print("Error: bank_reviews.csv not found. Ensure Task 1 output exists.")
    exit()

# Sentiment Analysis
def get_sentiment(text):
    try:
        analysis = TextBlob(str(text))
        polarity = analysis.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
        if polarity > 0:
            return "positive", polarity
        elif polarity < 0:
            return "negative", polarity
        else:
            return "neutral", polarity
    except:
        return "neutral", 0.0  # Fallback for errors

# Apply sentiment analysis
df['sentiment_label'], df['sentiment_score'] = zip(*df['review'].apply(get_sentiment))

# Thematic Analysis: Keyword Extraction
def extract_keywords(text):
    try:
        doc = nlp(str(text))
        # Extract nouns and adjectives as keywords, exclude stop words
        keywords = [token.text for token in doc if token.pos_ in ['NOUN', 'ADJ'] and not token.is_stop]
        return keywords[:5]  # Limit to top 5 keywords
    except:
        return []

# Apply keyword extraction
df['keywords'] = df['review'].apply(extract_keywords)

# Manual/Rule-Based Clustering into Themes
def assign_themes(keywords):
    keywords = [kw.lower() for kw in keywords]
    # Define simple rules for 2 themes per bank
    if any(kw in keywords for kw in ['crash', 'error', 'fail', 'bug', 'down']):
        return "Reliability Issues"
    elif any(kw in keywords for kw in ['slow', 'load', 'loading', 'delay', 'speed']):
        return "Performance Issues"
    else:
        return "Other"

# Apply theme assignment
df['identified_theme'] = df['keywords'].apply(assign_themes)

# Save results
df.to_csv('analyzed_reviews.csv', index=False, columns=[
    'review', 'rating', 'date', 'bank', 'source', 
    'sentiment_label', 'sentiment_score', 'identified_theme'
])

# Summary: Sentiment and themes per bank
for bank in df['bank'].unique():
    bank_df = df[df['bank'] == bank]
    print(f"\nAnalysis for {bank}:")
    print("Sentiment Distribution:")
    print(bank_df['sentiment_label'].value_counts())
    print("Theme Distribution:")
    print(bank_df['identified_theme'].value_counts())
    print(f"Sentiment scores calculated for {len(bank_df)} reviews")

print(f"\nSaved results to analyzed_reviews.csv")