from os import path, walk
from config import DOWNLOAD_FOLDER

def get_file_path_from_uuid(uuid):
    for (dirpath, dirname, filename) in walk(path.join(DOWNLOAD_FOLDER, uuid)):
        print(path.join(path.abspath(dirpath), filename[0]))
        return path.join(path.abspath(dirpath), filename[0])