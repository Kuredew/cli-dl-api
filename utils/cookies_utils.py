import os
import base64
import config

class Cookie:
    cookie_path = os.path.join(config.COOKIE_FOLDER, 'cookies.txt')

    def check_directory(self):
        return True if os.path.exists(config.COOKIE_FOLDER) else False

    def write_cookies_to_file(self, value):
        if not self.check_directory():
            os.makedirs(config.COOKIE_FOLDER)

        with open(self.cookie_path, 'w') as f:
            f.write(value)

    def get_cookie(self):
        cookie_base64 = str(config.COOKIE)
        cookie_decoded = base64.b64decode(cookie_base64.encode('ascii')).decode('ascii')

        self.write_cookies_to_file(cookie_decoded)
        return self.cookie_path
