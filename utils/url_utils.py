from services import YtdlpServices
import config

class Url:
    def __init__(self, url, format, reso):
        self.url = url
        self.reso = reso
        self.format = 'video' if format == 'v' else 'audio'

    def get_download_uuid(self):
        yt_dlp = YtdlpServices(self.url)
        uuid = yt_dlp.download(self.format, self.reso)

        if uuid:
            return uuid
    
        return False