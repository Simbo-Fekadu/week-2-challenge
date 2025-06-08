# 🚀 Week 2 Challenge: Customer Experience Analytics for Fintech Apps

Welcome to the Week 2 Challenge! This project focuses on analyzing customer experiences for leading Ethiopian fintech apps by leveraging user reviews from the Google Play Store.

---

## 📊 Overview

This challenge aims to extract actionable insights from real-world user feedback for three major banks:

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

By collecting and preprocessing app reviews, we lay the groundwork for deeper sentiment analysis and feature extraction in subsequent tasks.

---

## 📝 Task 1: Data Collection and Preprocessing

### 🎯 **Objective**

Scrape and preprocess Google Play Store reviews to build a clean dataset for analysis.

### 🛠️ **Methodology**

1. **Data Collection**

   - Utilized the [`google-play-scraper`](https://github.com/facundoolano/google-play-scraper) Python library.
   - Targeted 400+ reviews per bank, aiming for a total of **1,200+ reviews**.
   - Extracted the following fields:
     - **Review Text**
     - **Rating** (1-5 stars)
     - **Date**
     - **Bank Name**
     - **Source** (Google Play)

2. **Preprocessing Steps**
   - **Removed duplicates** to ensure unique feedback.
   - **Dropped rows** with missing review text for data quality.
   - **Normalized dates** to `YYYY-MM-DD` format for consistency.
   - **Saved** the cleaned dataset as [`bank_reviews.csv`](./bank_reviews.csv).

### 🧰 **Tools Used**

- Python
- `google-play-scraper`
- `pandas`

### 📈 **Status**

- **Total Reviews Collected:** **1,250** (exceeding the initial target!)
- Dataset is ready for further analysis.

---

## 📂 Project Structure

```
week-2-challenge/
├── README.md
├── bank_reviews.csv
├── data_collection.py
└── requirements.txt
```

---

## 🚦 Next Steps

## 🧠 Task 2: Sentiment & Thematic Analysis

### 🎯 **Objective**

Quantify user sentiment and uncover key themes in reviews for CBE, BOA, and Dashen Bank.

### 🛠️ **Methodology**

- **Sentiment Analysis:**

  - Applied [TextBlob](https://textblob.readthedocs.io/) to classify reviews as positive, negative, or neutral.
  - Calculated sentiment polarity scores for each review.

- **Thematic Analysis:**

  - Initiated keyword and topic extraction using [spaCy](https://spacy.io/).
  - Currently resolving spaCy model installation issues to finalize theme identification.

- **Output:**
  - Results saved to [`analyzed_reviews.csv`](./analyzed_reviews.csv), including sentiment labels and scores.

### 🧰 **Tools Used**

- Python
- TextBlob
- spaCy (in progress)

### 📈 **Status**

- **Sentiment analysis:** Complete on all collected reviews.
- **Thematic analysis:** In progress—final results pending spaCy setup.

- **Task 3:** Visualization and reporting.
