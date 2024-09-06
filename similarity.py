import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch
import json

# Load the Excel file and both sheets
file_path = 'inputFiles/test_files.xlsx'
sheet_a = pd.read_excel(file_path, sheet_name='File_A')
sheet_b = pd.read_excel(file_path, sheet_name='File_B')

# Extract male and female names based on the 'Gender' column
male_names_a = sheet_a[sheet_a['Gender'] == 'M']['Student Name'].tolist()
female_names_a = sheet_a[sheet_a['Gender'] == 'F']['Student Name'].tolist()

male_names_b = sheet_b[sheet_b['Gender'] == 'M']['Student Name'].tolist()
female_names_b = sheet_b[sheet_b['Gender'] == 'F']['Student Name'].tolist()

# Combine male and female names from both sheets
male_names = male_names_a + male_names_b
female_names = female_names_a + female_names_b

# Load the LaBSE model
model = SentenceTransformer('sentence-transformers/LaBSE')

# Encode male and female names
male_embeddings = model.encode(male_names, convert_to_tensor=True)
female_embeddings = model.encode(female_names, convert_to_tensor=True)

# Compute the cosine similarity between male and female names
similarity_matrix = util.pytorch_cos_sim(male_embeddings, female_embeddings)

# Convert similarity matrix to numpy array for easier manipulation
similarity_scores = similarity_matrix.cpu().numpy()

# Set the similarity threshold to 0.50
threshold = 0.50
similar_pairs = []

# Collect results with similarity >= 50%
for i, male_name in enumerate(male_names):
    for j, female_name in enumerate(female_names):
        score = similarity_scores[i, j]
        if score >= threshold:
            similar_pairs.append({
                "male_name": male_name,
                "female_name": female_name,
                "similarity": float(score)
            })

# Saving the results to a JSON file
output_file = 'outputFiles/male_female_similarity.json'
with open(output_file, 'w') as f:
    json.dump(similar_pairs, f, indent=4)

print(f"Results saved to {output_file}")