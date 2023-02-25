import requests
from config import TOKEN


class FOLDER_IN_YANDEX:

    URL = 'https://cloud-api.yandex.net/'

    def __init__(self, title):
        self.title = title

    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {TOKEN}'
        }

    def create_folder(self):
        uri = 'v1/disk/resources'
        folder_url = self.URL + uri
        folder = requests.put(folder_url, params={'path': self.title}, headers=self.headers())

        return folder.status_code

f = FOLDER_IN_YANDEX('Папка')
status_code = f.create_folder()
folder_name = f.title


