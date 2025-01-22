import spacy
import pandas as pd
import json

# Load SpaCy's pre-trained model for NER
nlp = spacy.load('en_core_web_sm')

# Use the absolute path for the CSV file
df = pd.read_csv(r'F:\M.Tech_CollgeMaterials\Ner_System\data\processed_data\news\cnbc_headlines_processed.csv')

# Function to annotate entities using SpaCy
def annotate_text(text):
    doc = nlp(text)
    annotations = []
    
    # Extract entities and their start/end positions
    for ent in doc.ents:
        annotations.append({
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_
        })
    
    return annotations

# List to store annotated data
annotated_data = []

# Iterate over each row in the DataFrame and annotate the text
for index, row in df.iterrows():
    text = row['standardized_text']  # Use the 'standardized_text' column for annotation
    annotations = annotate_text(text)
    
    # Append the annotated text and its entities to the list
    annotated_data.append({
        "headline": row['Headlines'],
        "text": text,
        "entities": annotations
    })

# Save the annotated data to a JSON file
output_file_path = 'annotated_data.json'
with open(output_file_path, 'w') as json_file:
    json.dump(annotated_data, json_file, indent=4)

print(f"Annotations saved to '{output_file_path}'.")
