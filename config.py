import os
from dotenv import load_dotenv

load_dotenv()

# TODO: приведение типов
DEBUG = os.getenv("DEBUG", "False")          # строка! "False" истинна
PORT = os.getenv("PORT", "8000")             # строка!
MAX_REPOS = os.getenv("MAX_REPOS", "10")     # строка! ломает срез в /stats
ENABLE_CACHE = os.getenv("ENABLE_CACHE", "0")# строка! "0" истинна
GITHUB_LOGIN = os.getenv("GITHUB_LOGIN", "octocat")
