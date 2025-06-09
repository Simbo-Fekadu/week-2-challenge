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
├── requirements.txt
├── analyzed_reviews.csv
├── setup_database.sql
├── insert_reviews.py
├── bank_reviews_dump.dmp
├── query_insights.sql
├── visualize_insights.py
├── generate_insights.py
├── insights_report.md
├── images/
│   ├── avg_rating_by_bank.png
│   ├── sentiment_distribution.png
│   ├── top_themes.png
│   └── reviews_by_month.png
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

---

## 🗄️ Task 3: Store Cleaned Data in Oracle

### 🎯 **Objective**

Design and implement a robust relational database in Oracle to securely store and manage the processed review data for further querying and analysis.

### 🛠️ **Methodology**

1. **Database Setup**

- Installed **Oracle Database Express Edition (XE)** for a lightweight, local RDBMS environment.
- Configured environment variables by adding the Oracle bin directory (`C:\app\Simbo\product\21c\dbhomeXE\bin`) to the system `PATH` for seamless command-line access.

2. **Schema Design**

- Created a normalized schema with two main tables:
  - **`banks`**: Stores unique bank identifiers and names.
  - **`reviews`**: Stores all review details, including foreign keys referencing the `banks` table.
- Ensured referential integrity and optimized for analytical queries.

3. **Table Creation & Initialization**

- Authored [`setup_database.sql`](./setup_database.sql) to:
  - Create the required tables with appropriate data types and constraints.
  - Insert initial bank records into the `banks` table.

4. **Data Ingestion**

- Developed [`insert_reviews.py`](./insert_reviews.py) to:
  - Read the cleaned and analyzed data from [`analyzed_reviews.csv`](./analyzed_reviews.csv).
  - Insert review records into the `reviews` table using the [oracledb](https://python-oracledb.readthedocs.io/en/latest/) Python package.
  - Handle data type conversions and ensure transactional integrity.

5. **Backup & Export**

- Exported the populated database as a SQL dump file: [`bank_reviews_dump.dmp`](./bank_reviews_dump.dmp) for backup and portability.

### 🧰 **Tools Used**

- **Python** (for scripting and data loading)
- **oracledb** (Python-Oracle connectivity)
- **Oracle Database XE** (database engine)
- **SQL** (schema and data manipulation)

### 📈 **Status**

- **Database schema:** Designed and deployed.
- **Data ingestion:** Successfully loaded all analyzed reviews into Oracle.
- **Backup:** SQL dump exported for safekeeping.
- **Total Reviews Stored:** **1,250** entries (matching the processed dataset).

---

## 📊 Task 4: Generate Insights and Visualizations

### 🎯 **Objective**

Analyze bank review data to extract insights and create visualizations.

### 🛠️ **Methodology**

- Queried Oracle database (or used `analyzed_reviews.csv`) for average ratings, sentiment distribution, top themes, and review trends.
- Used `query_insights.sql` for SQL queries.
- Generated visualizations (bar, pie, line charts) with `visualize_insights.py`.
- Summarized findings in `insights_report.md` using `generate_insights.py`.

### 🧰 **Tools Used**

- Python
- pandas
- matplotlib
- seaborn
- Oracle XE

### 📈 **Outputs**

- **Visualizations:**
  - ![Average Rating by Bank](./images/avg_rating_by_bank.png)
  - ![Sentiment Distribution](./images/sentiment_distribution.png)
  - ![Top Themes](./images/top_themes.png)
  - ![Reviews by Month](./images/reviews_by_month.png)
- **Report:** See [`insights_report.md`](./insights_report.md) for summarized findings.

---
