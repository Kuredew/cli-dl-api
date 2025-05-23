from yt_dlp import YoutubeDL
from utils import Logging
import uuid
import config

class YtdlpServices:
    def __init__(self, url):
        self.url = url
        self.uuid = str(uuid.uuid4())
        self.output_folder = config.DOWNLOAD_FOLDER + '/' + self.uuid + '/'

    def download(self, format, reso=None, convert='false'):
        if format == 'video':
            ydl_opts = {
                'format_sort': [f'res:{reso}'],
                'format': 'bv*+ba'
            }
        elif format == 'audio':
            ydl_opts = {
                'format': 'ba',
                'postprocessing': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredCodec': 'mp3'
                }]
            }
        
        ydl_opts['outtmpl'] = f'{self.output_folder}%(title)s.%(ext)s'
        ydl_opts['quiet'] = True

        if convert == 'true':
            ydl_opts['postprocessing'] = [{
                'key': 'FFmpegVideoConvertor',
                'preferredCodec': 'h264',
                'preferredFormat': 'mp4'
            }]

        print(ydl_opts)

        try:
            with YoutubeDL(ydl_opts) as ydl:
                Logging.info('Start downloading at ' + self.url + ' to ' + self.output_folder)
                ydl.download(self.url)

                #ydl.download_with_info_file(info)

                return self.uuid

        except Exception as e:
            Logging.error(f'yt-dlp error : {e}')
            Logging.error('Stopping program.')
            return False