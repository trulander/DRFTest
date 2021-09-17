from __future__ import print_function

import io
import os.path


from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
from googleapiclient.http import MediaIoBaseDownload

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.metadata'
]


def main():

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)


    filder_id = '-'

    ''' id файла базы данных на гугл диске с которым нужно работать.'''
    file_id = '-'

    request = service.files().get_media(fileId=filder_id)
    items = request.get('files', [])
    items

    # with open('111', 'wb') as fh:
    #     downloader = MediaIoBaseDownload(fh, request)
    #     done = False
    #     while done is False:
    #         status, done = downloader.next_chunk()
    #         print("Download %d%%. % int(status.progress() * 100)")




if __name__ == '__main__':
    main()