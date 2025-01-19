# Preprocessing new_articles datasets 

import pandas as pd
import spacy
import re
import os

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Increase the SpaCy document length limit
nlp.max_length = 20000000  # Increase max length to handle longer documents

# Function to load the dataset (including SEC files)
def load_data(file_path):
    # If it's a CSV, read it as a pandas DataFrame
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    
    # If it's a plain text file, read it and return as a single document
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return pd.DataFrame({'text': [file.read()]})
    
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

# Function to clean the text
def clean_text(text):
    if pd.isna(text):  # Check if the text is NaN
        return ""
    text = str(text)  # Convert non-string types to string
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text

# Function to standardize financial terms
def standardize_terms(text):
    terms_dict = {
        'usd': 'U.S. dollars',
        '$': 'U.S. dollars',
        'q1': 'Q1',
        'q2': 'Q2',
        'q3': 'Q3',
        'q4': 'Q4',
    }
    for term, replacement in terms_dict.items():
        text = text.replace(term, replacement)
    return text

# Function to tokenize the text using SpaCy
def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop]
    return tokens

# Function to split long text into smaller chunks
def split_long_text(text, max_length=1000000):
    """Split a long text into smaller chunks that SpaCy can handle."""
    # Split text into chunks of up to max_length characters
    text_length = len(text)
    if text_length <= max_length:
        return [text]  # Return the text as a single chunk if it's small enough
    else:
        # Split the text into chunks of max_length
        num_chunks = (text_length // max_length) + 1
        return [text[i * max_length:(i + 1) * max_length] for i in range(num_chunks)]

# Preprocessing pipeline function for both SEC and news data
def preprocess_data(file_path):
    df = load_data(file_path)
    
    # Check if the column 'text' exists, otherwise use the first column as fallback
    column_name = 'text' if 'text' in df.columns else df.columns[0]
    
    # Apply cleaning, standardization, and tokenization
    df['cleaned_text'] = df[column_name].apply(clean_text)
    df['standardized_text'] = df['cleaned_text'].apply(standardize_terms)
    
    # Handle long text splitting and tokenize each chunk
    df['tokens'] = df['standardized_text'].apply(lambda x: [token for chunk in split_long_text(x) for token in tokenize_text(chunk)])
    
    return df

# List of files to process (news articles + SEC filings)
files_to_process = [
    r'F:\M.Tech_CollgeMaterials\Ner_System\data\rawdata\news_articles\cnbc_headlines.csv',  
    r'F:\M.Tech_CollgeMaterials\Ner_System\data\rawdata\news_articles\guardian_headlines.csv',
    r'F:\M.Tech_CollgeMaterials\Ner_System\data\rawdata\news_articles\reuters_headlines.csv'
]

# Process each file and save the preprocessed output
for file_path in files_to_process:
    # Process the file
    processed_df = preprocess_data(file_path)
    
    # Create a folder for processed data if it doesn't exist
    os.makedirs('data/processed_data/news', exist_ok=True)
    
    # Extract the base name from the file path (remove extension)
    base_name = os.path.basename(file_path).split('.')[0]
    
    # Modify the output file path for the processed data
    output_file_path = os.path.join('data/processed_data/news', f'{base_name}_processed.csv')
    
    # Save the processed data to a new CSV file
    processed_df.to_csv(output_file_path, index=False)
    
    # Print a preview of the processed data
    print(f"Processed file saved: {output_file_path}")
    print(processed_df.head())  # Display first few rows to confirm processing
