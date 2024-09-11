import pandas as pd
import logging
import re

# logging config
logging.basicConfig(filename='app.log', level=logging.INFO)


def main():
    # load data from excel files
    all_sheets = pd.read_excel('test_files.xlsx', sheet_name=None)

    # combine all sheets into a single data source for all the data in both file a and b to be read
    df = pd.concat(all_sheets.values(), ignore_index=True)

    print(df.columns)
    # checks column names for gender and student name if they do exist in the data source
    if 'Gender' not in df.columns:
        raise ValueError("Data does not contain a 'Gender' column")

    # standardizes male and female students
    males = df[df['Gender'].str.strip().str.lower() == 'm']
    females = df[df['Gender'].str.strip().str.lower() == 'f']

    # save to csv files
    males.to_csv('males.csv', index=False)
    females.to_csv('females.csv', index=False)

    # save to tsv
    males.to_csv('males.tsv', sep='\t', index=False)
    females.to_csv('females.tsv', sep='\t', index=False)

    # log the numbers of students per gender
    logging.info(f"Number of male students: {len(males)}")
    logging.info(f"Number of female students: {len(females)}")

    # define the regex pattern for special characters(removed comma bc every name has it)
    pattern = r'[!@#$%^&*()_+{}[\]:;"\'<>.?/\\|`~]'

    # check for special characters in names
    if 'Student Name' in df.columns:
        names_with_special_chars = df[df['Student Name'].str.contains(pattern, regex=True)]

        # list names with special characters
        special_char_names = names_with_special_chars['Student Name'].tolist()
        print("Names with special characters:")
        for name in special_char_names:
            print(name)

        # save to csv
        special_char_names_df = pd.DataFrame(special_char_names, columns=['Name'])
        special_char_names_df.to_csv('special_char_names.csv', index=False)
        special_char_names_df.to_csv('special_char_names.tsv', sep='\t', index=False)

    else:
        logging.error("The data source does not contain 'Student Name' column.")

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
            
# Ensure the script is executed directly
if _name_ == "_main_":
    main()