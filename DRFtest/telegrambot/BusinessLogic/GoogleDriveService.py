from __future__ import print_function

import os.path
from typing import Union

import googleapiclient
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

from ..Core.Exceptions import GoogleDriveFileException
from ..Core.GoogleDriveServiceInterface import GoogleDriveServiceItnerface

class GoogleDriveService(GoogleDriveServiceItnerface):
    _service: googleapiclient.discovery
    _file_name: str
    _folder_id: str
    _token_json_path: str
    _credential_json_path: str

    SCOPES = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.metadata'
    ]


    def __init__(self):
        self._file_name = 'bluecoins.fydb'
        self._folder_id = '-'
        self._token_json_path = 'token.json'
        self._credential_json_path = 'credentials.json'
        self._service =  self._connect_google_drive()


    def syncDb(self):
        file_id = self._find_file_by_name_in_folder_by_id(folder_id=self._folder_id, file_name=self._file_name)

        if not self._load_file_by_id_save_by_name(file_id=file_id, file_name=self._file_name):
            raise GoogleDriveFileException('Somethink hapaned and file wasn\'t downloaded')


    def _connect_google_drive(self) -> googleapiclient.discovery:

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self._token_json_path):
            creds = Credentials.from_authorized_user_file(self._token_json_path, self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self._credential_json_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self._token_json_path, 'w') as token:
                token.write(creds.to_json())

        return build('drive', 'v3', credentials=creds)


    def _find_file_by_name_in_folder_by_id(self, folder_id: str, file_name: str) -> Union[None, str]:

        results = self._service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            pageSize=2,
            fields="nextPageToken, files(id, name)"
        ).execute()
        items = results.get('files', [])

        if items:
            for item in items:
                if file_name == item['name']:
                    return item['id']

        return None


    def _load_file_by_id_save_by_name(self, file_id: str, file_name: str) -> bool:

        request = self._service.files().get_media(fileId=file_id)

        with open(file_name, 'wb') as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()

            return done


    def _upload_new_file(self, local_path_to_file: str, new_file_name: str, folder_id: str) -> str:
        file_metadata = {
            'name': new_file_name,
            'parents': [folder_id]
        }

        media_content = MediaFileUpload(local_path_to_file)
        file = self._service.files(
            body=file_metadata,
            media_body=media_content
        ).execute()

        return file['id']


    def _update_old_file(self, file_id, local_path_to_file: str):
        self._service.files().update(
            fileid=file_id,
            media_body= MediaFileUpload(local_path_to_file)
        ).execute()