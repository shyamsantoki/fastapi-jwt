from os import getenv

from dotenv import load_dotenv

load_dotenv()

DRIVER = getenv("DB_DRIVER")
USERNAME = getenv("DB_USERNAME")
PASSWORD = getenv("DB_PASSWORD")
HOST = getenv("DB_HOST")
PORT = getenv("DB_PORT")
DATABASE = getenv("DB_DATABASE")
SQLALCHEMY_URL = f"{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
