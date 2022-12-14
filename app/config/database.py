from os import getenv
from dotenv import load_dotenv

load_dotenv()

DRIVER = os.getenv("DB_DRIVER")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_DATABASE")
SQLALCHEMY_URL = f"{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
