import pandas as pd

import json

# Assuming your data is in a CSV file called "names.csv"
df = pd.read_csv("names.csv")

# Shuffle the names
df = df.sample(frac=1).reset_index(drop=True)

# 1. Save as a JSON file
df.to_json("shuffled_names.json", orient="records") 

# 2. Save as a JSONL file
with open("shuffled_names.jsonl", "w") as f:
    for i in range(len(df)):
        json.dump(df.iloc[i].to_dict(), f)
        f.write("\n")