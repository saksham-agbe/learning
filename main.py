from pathlib import Path
from dotenv import load_dotenv
import os


env_path = Path(__file__).parent / ".env"
load_dotenv(env_path) 



DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")
print(f"{DATABASE_URL},{SECRET_KEY},{DEBUG }")







# from src.conditions import check_if, check_else, check_elif, check_statement, check_vote

# check_if()
# check_else()
# check_elif()
# check_statement()
# check_vote()
