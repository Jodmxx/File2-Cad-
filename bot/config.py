from os import environ as env



class Telegram:

    API_ID = int(env.get("TELEGRAM_API_ID", 19160495))

    API_HASH = env.get("TELEGRAM_API_HASH", "0e98cc48b081a829a86c593cdfdd720d")

    OWNER_ID = int(env.get("OWNER_ID", 2010387571))

    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()

    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Jodfor_bot")

    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "5627926616:AAF-wfPHDRWJJNfqgU0WDKdAE_XaWORSHtw")

    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001996145098))

    BOT_WORKERS = int(env.get("BOT_WORKERS", 10))

    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))



class Server:

    BASE_URL = env.get("BASE_URL", "https://hlwe-ee1a0121919e.herokuapp.com")

    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")

    PORT = int(env.get("PORT", ))



# LOGGING CONFIGURATION

LOGGER_CONFIG_JSON = {

    'version': 1,

    'formatters': {

        'default': {

            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',

            'datefmt': '%d/%m/%Y %H:%M:%S'

        },

    },

    'handlers': {

        'file_handler': {

            'class': 'logging.FileHandler',

            'filename': 'event-log.txt',

            'formatter': 'default'

        },

        'stream_handler': {

            'class': 'logging.StreamHandler',

            'formatter': 'default'

        }

    },

    'loggers': {

        'uvicorn': {

            'level': 'INFO',

            'handlers': ['file_handler', 'stream_handler']

        },

        'uvicorn.error': {

            'level': 'WARNING',

            'handlers': ['file_handler', 'stream_handler']

        },

        'bot': {

            'level': 'INFO',

            'handlers': ['file_handler', 'stream_handler']

        }

    }

}
