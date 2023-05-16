import os
from dotenv import load_dotenv


def get_default_sleep():
    load_dotenv()
    return float(os.getenv('DEFAULT_SLEEP'))
