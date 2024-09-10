import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']


# Authenticate and get Google Drive service
def authenticate_drive_api():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


# Create a folder in Google Drive
def create_drive_folder(service, folder_name, parent_folder_id=None):
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    if parent_folder_id:
        file_metadata['parents'] = [parent_folder_id]

    folder = service.files().create(body=file_metadata, fields='id').execute()
    print(f"Created folder: {folder_name}, ID: {folder.get('id')}")
    return folder.get('id')


# Upload file to Google Drive
def upload_file_to_drive(service, file_path, folder_id):
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]  # Set the folder where this file should be uploaded
    }

    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"Uploaded file: {file_path}, ID: {file.get('id')}")


# Recursively upload a folder
def upload_folder_to_drive(service, local_folder_path, parent_folder_id=None):
    # Create a folder in Google Drive
    folder_name = os.path.basename(local_folder_path)
    folder_id = create_drive_folder(service, folder_name, parent_folder_id)

    # Traverse the local folder and upload files/subfolders
    for root, dirs, files in os.walk(local_folder_path):
        # Upload each file in the directory
        for file_name in files:
            file_path = os.path.join(root, file_name)
            upload_file_to_drive(service, file_path, folder_id)

        # Recursively upload subfolders
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            upload_folder_to_drive(service, dir_path, folder_id)


# Main function to upload a folder to Google Drive
def backup_folder_to_google_drive(folder_path):
    creds = authenticate_drive_api()
    service = build('drive', 'v3', credentials=creds)

    upload_folder_to_drive(service, folder_path)


# Replace this with your local folder path
local_folder_path = "D:\Projects\student_codelab"
backup_folder_to_google_drive(local_folder_path)
