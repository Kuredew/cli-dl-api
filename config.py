from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv('HOST', 'http://127.0.0.1:5000')
DOWNLOAD_PATH = getenv('DOWNLOAD_PATH', 'download')
DOWNLOAD_FOLDER = getenv('DOWNLOAD_FOLDER', 'downloads')

COOKIE = getenv('COOKIE', 'Z2V0IHNvbWUgd29yayBicm8h')
COOKIE_PATH = getenv('COOKIE_PATH', 'cookies/cookies.txt')