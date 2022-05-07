import logging

from environs import Env

env = Env()

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}
LOG_LEVEL_STR = env.str("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = LOG_LEVELS.get(LOG_LEVEL_STR)

UTR_URL = "https://app.universaltennis.com/api"
UTR_EMAIL = env.str("UTR_EMAIL")
UTR_PASSWORD = env.str("UTR_PASSWORD")
