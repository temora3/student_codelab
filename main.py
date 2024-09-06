import pandas as pd
import logging
import re

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    # Load the data from the Excel file
    all_sheets = pd.read_excel('test_files.xlsx', sheet_name=None)

    # Combine all sheets into a single DataFrame
    df = pd.concat(all_sheets.values(), ignore_index=True)

    # Verify column names
    print(df.columns)  # Check column names for 'Gender', 'First Name', 'Last Name'

    # Ensure there is a 'Gender' column
    if 'Gender' not in df.columns:
        raise ValueError("Data does not contain a 'Gender' column")

    # Create separate lists for male and female students
    males = df[df['Gender'].str.strip().str.lower() == 'm']
    females = df[df['Gender'].str.strip().str.lower() == 'f']

    # Save the separate lists to CSV files
    males.to_csv('males.csv', index=False)
    females.to_csv('females.csv', index=False)

    # Save to TSV
    males.to_csv('males.tsv', sep='\t', index=False)
    females.to_csv('females.tsv', sep='\t', index=False)

    # Log the number of male and female students
    logging.info(f"Number of male students: {len(males)}")
    logging.info(f"Number of female students: {len(females)}")

    # Define the regex pattern for special characters
    pattern = r'[!@#$%^&*()_+{}\[\]:;"\'<>.?/\\|`~]'

    # Check for special characters in names
    if 'Student Name' in df.columns:
        names_with_special_chars = df[df['Student Name'].str.contains(pattern, regex=True)]

        # List names with special characters
        special_char_names = names_with_special_chars['Student Name'].tolist()
        print("Names with special characters:")
        for name in special_char_names:
            print(name)

        # Save to CSV
        special_char_names_df = pd.DataFrame(special_char_names, columns=['Name'])
        special_char_names_df.to_csv('special_char_names.csv', index=False)
        special_char_names_df.to_csv('special_char_names.tsv',sep='\t', index=False)


    else:
        logging.error("The DataFrame does not contain 'Student Name' columns.")
    
    #Merge the male and femal students TSV files
    male_students = pd.read_csv('male_students.tsv', sep='\t')
    female_students = pd.read_csv('female_students.tsv', sep='\t')
    
    #Concatenate the data
    all_students = pd.concat([male_students, female_students])
    
    # Reset the index
    all_students.reset_index(drop=True, inplace=True)

    # Shuffle the data
    shuffled_students = all_students.sample(frac=1).reset_index(drop=True)

    # Save as JSON file
    shuffled_students.to_json('shuffled_students.json', orient='records')

    # Save as JSONL file
    with open('shuffled_students.jsonl', 'w') as f:
        for index, row in shuffled_students.iterrows():
            json.dump(row.to_dict(), f)
            f.write('\n')
        

if __name__ == "__main__":
    main()