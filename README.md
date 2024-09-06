# Student Email Generator and Data Processor

## Overview

This project processes student data from an Excel file to generate unique email addresses, categorize students by gender, identify names with special characters, as well as perform additional similarity checks. It uses Python libraries like Pandas and LaBSE to do so. The processed data is saved in multiple formats such as CSV, TSV, JSON, and JSONL.

## Features

- *Generate Unique Email Addresses*: Create email addresses for students based on their names.
- *Gender Categorization*: Separate students into male and female lists.
- *Special Character Identification*: List names containing special characters.
- *Similarity Analysis*: Compare male and female names using LaBSE and identify similar names.
- *Data Formatting and Export*: Save processed data in CSV, TSV, JSON, and JSONL formats.
- *Backup to Google Drive*: Use Google API for cloud storage backup.

## Requirements

- Python 3.8 or higher
- Pandas
- LaBSE
- Tensorflow
- Google API (for cloud storage)
- Openpyxl (for reading and writing to the Excel file)

## Setup

### 1. Create a New Environment

Create a virtual environment and activate it:

bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\\Scripts\\activate`



### 2. Install Required Libraries

Install the necessary Python libraries:

bash
pip install pandas
pip install google-api-python-client  # For Google API
pip install tensorflow
pip install openpyxl



### 3. Download Test Files

Download the test file test_files.xlsx and place it in the project directory.

## Usage

### 1. Run the Main Program

Execute the main program to process the data:

bash
python main.py



### 2. Check the Output

- *CSV Files*: males.csv, females.csv
- *TSV Files*: males.tsv, females.tsv
- *Names with Special Characters*: special_char_names.csv,special_char_names.tsv

### 3. View Logs

Logs of computations are saved in app.log.

## File Descriptions

- [*main.py*](http://main.py/): Main program file that coordinates the workflow.

## How to Contribute

1. *Fork the Repository*: Create a fork of this repository to your own GitHub account.
2. *Clone Your Fork*: Clone the forked repository to your local machine.
3. *Create a Branch*: Create a new branch for your changes.
4. *Make Changes*: Implement your changes and commit them.
5. *Push Changes*: Push changes to the forked repository.
6. *Create a Pull Request*: Open a pull request from the forked repository to the main repository.

## Additional Information

- *LaBSE Similarity Analysis*: To run a similarity check on the student names, use LaBSE.
- *Google API Key*: To back up your data to Google Drive, generate a Google API key and configure it in your project.

## License

This project is licensed under the MIT License. See the [LICENSE](https://www.notion.so/LICENSE) file for details.

## Acknowledgments

- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [LaBSE Documentation](https://github.com/google-research/bert/blob/master/docs/LaBSE.md)
- [Google API Documentation](https://developers.google.com/drive/api/v3/about-sdk)