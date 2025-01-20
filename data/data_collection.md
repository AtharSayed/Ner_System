# Data Collection

## Overview

This document describes the process of collecting and preprocessing the data for the `Ner_System` project. The data is sourced from two primary datasets:

1. **Financial News Articles**: Headlines collected from financial news agencies such as CNBC, The Guardian, and Reuters.
2. **Financial Reports**: A Kaggle dataset titled `financial-q-and-a-10k` that contains detailed financial Q&A data and reports.

Both datasets are processed to clean the text, standardize financial terms, and prepare the data for analysis and machine learning tasks.

---

## Data Sources

### 1. Financial News Articles

The raw data for financial news articles is sourced from publicly available datasets that include financial headlines from three major news agencies:

- **CNBC Headlines**: Headlines from CNBC, focused on financial news.
- **The Guardian Headlines**: Headlines from The Guardian, with a focus on finance.
- **Reuters Headlines**: Headlines from Reuters, covering various financial topics.

These datasets are stored in the `data/raw_data/news_articles/` directory. The files include the following CSV files:

- `cnbc_headlines.csv`
- `guardian_headlines.csv`
- `reuters_headlines.csv`

Each CSV contains columns such as `headline` and `date`, with the actual text data stored in the `text` column.

### 2. Financial Reports

The second dataset comes from Kaggle and is titled **`financial-q-and-a-10k`**. This dataset includes a collection of financial question-answer pairs and detailed financial reports, which provide context for analyzing financial news.

You can access this dataset on Kaggle at the following link:

- **Financial Q&A 10k**: [Financial Q&A 10k Dataset on Kaggle](https://www.kaggle.com/datasets/yousefsaeedian/financial-q-and-a-10k)

The dataset is available in `.csv` and `.txt` formats, and is processed similarly to the news article datasets.

---

## Data Preprocessing

The raw data is preprocessed to ensure that it is clean, consistent, and suitable for analysis and machine learning tasks. The preprocessing steps include the following:

### 1. Data Cleaning

The text data is cleaned by performing the following steps:

- **Removing Punctuation**: All punctuation and special characters are removed.
- **Lowercasing**: The entire text is converted to lowercase to maintain consistency.
- **Removing Digits**: All numerical values are removed, as they do not contribute meaningful information for certain types of analysis.
- **Whitespace Handling**: Extra spaces between words are replaced with a single space to ensure consistency.

### 2. Standardizing Financial Terms

To ensure consistency across the dataset, financial terms and abbreviations are standardized:

- `USD`, `$` → `U.S. dollars`
- `Q1`, `Q2`, `Q3`, `Q4` → `Q1`, `Q2`, `Q3`, `Q4` (Standardized quarter terms)

This step helps maintain uniformity when analyzing financial data.

### 3. Tokenization

The text is tokenized into individual words (or tokens) using the **SpaCy** NLP library. During tokenization, common stopwords (e.g., "the", "and") are removed to reduce noise in the data.

### 4. Handling Long Texts

For longer documents (particularly in the case of financial reports), the text is split into smaller chunks to ensure they can be processed efficiently. Each chunk is then tokenized separately.

### 5. Saving Processed Data

After preprocessing, the cleaned and tokenized data is saved as new CSV files in the `data/processed_data/` directory. This ensures that the original raw data remains intact, while the processed data is ready for analysis.

---

## Conclusion

This document has outlined the process of collecting and preprocessing the data used in the `Ner_System` project. The data comes from two main sources: financial news articles and financial reports. The raw data is cleaned, standardized, tokenized, and saved in a format suitable for further analysis and model training.

For detailed information on the preprocessing steps, refer to this code file where i did processing : `data/processed_data/preprocess_data.py` 
