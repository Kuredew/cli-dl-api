import config
import base64

def write_cookies_to_file(value):
    with open(config.COOKIE_PATH, 'w') as f:
        f.write(value)

def get_cookie():
    cookie_base64 = str(config.COOKIE)
    cookie_decoded = base64.b64decode(cookie_base64.encode('ascii')).decode('ascii')

    write_cookies_to_file(cookie_decoded)
    return config.COOKIE_PATH
