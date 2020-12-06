import os

from dotenv import load_dotenv

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(PROJECT_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

