# (c) Code-x-Mania

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID','25079224'))
    API_HASH = str(getenv('API_HASH','0b0a38787359e75477c47ef7c01ea8fd'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','6226448350:AAF0SnZYDnQtHuNsTAUxplV_WOnJWeMZDvg'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'F2LxBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001953488313'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    #OWNER_ID = int(getenv('OWNER_ID', '2068472689'))
    OWNER_ID = "661054276"
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = 'mrprince'
    OWNER_USERNAME = str(getenv('OWNER_USERNAME'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL','mongodb+srv://filetolink:filetolink@filetolink.a4zbbrj.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS")).split()))
