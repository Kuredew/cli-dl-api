from utils import Url
import config

class Urls:
    def __init__(self, url, format, reso):
        self.url = url
        self.format = format
        self.reso = reso

    def get_json(self):
        return {
            'ok': None,
            'url': self.url,
            'download_url': None
        }

    def pass_info(self, is_ok, uuid=None):
        json = self.get_json()
        
        if is_ok:
            json['ok'] = True
            json['download_url'] = f'{config.HOST}/{config.DOWNLOAD_PATH}/{uuid}'
        else:
            json['ok'] = False

        return json

    def get_info(self):
        uuid = Url(self.url, self.format, self.reso).get_download_uuid()

        if uuid:
            return self.pass_info(True, uuid)
        else:
            return self.pass_info(False)

