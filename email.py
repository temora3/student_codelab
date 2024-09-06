import pandas as pd
import re

# Load the Excel file with both sheets
file_path = "inputFiles/test_files.xlsx"  # Change this to your actual file path
xls = pd.ExcelFile(file_path)

# Load both sheets into separate dataframes
df1 = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
df2 = pd.read_excel(xls, sheet_name=xls.sheet_names[1])

# Function to generate email addresses
def generate_email(name):
    # Remove special characters from the name (retain spaces and comma)
    name = re.sub(r"[^a-zA-Z\s,]", "", name)

  # Split the name by comma
    try:
        last_name, first_name = [n.strip() for n in name.split(",")]
    except ValueError:
        return None  # Handle cases where the name doesn't have a comma

    # Use the first letter of the first name after the comma and the last name before the comma
    first_letter = first_name[0].lower() if first_name else ""
    last_name = last_name.lower()

    # Remove spaces and special characters from the last name
    email_prefix = first_letter + re.sub(r"[^a-zA-Z]", "", last_name)

    # Construct the email
    email = f"{email_prefix}@gmail.com"

    return email


# Apply the function to both dataframes
df1["Email Address"] = df1["Student Name"].apply(generate_email)
df2["Email Address"] = df2["Student Name"].apply(generate_email)


# Make sure the emails are unique
def ensure_unique_emails(df):
    emails = set()
    for i, email in enumerate(df["Email Address"]):
        original_email = email
        counter = 1
        # If the email is not unique, append a counter to make it unique
        while email in emails:
            email = f"{original_email.split('@')[0]}{counter}@gmail.com"
            counter += 1
        emails.add(email)
        df.at[i, "Email Address"] = email

# Ensure unique emails in both dataframes
ensure_unique_emails(df1)
ensure_unique_emails(df2)

# Write back to the Excel file, updating the sheets
with pd.ExcelWriter(file_path, mode="a", if_sheet_exists="replace") as writer:
    df1.to_excel(writer, sheet_name=xls.sheet_names[0], index=False)
    df2.to_excel(writer, sheet_name=xls.sheet_names[1], index=False)

print("Email addresses generated and saved back to the Excel file.")

