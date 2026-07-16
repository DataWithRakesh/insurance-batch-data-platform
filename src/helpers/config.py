from pathlib import Path
from dotenv import load_dotenv
import os


# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env from project root
load_dotenv(BASE_DIR / ".env")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

print("SQL_SERVER :", SQL_SERVER)
print("SQL_DATABASE :", SQL_DATABASE)
print("SQL_USERNAME :", SQL_USERNAME)
