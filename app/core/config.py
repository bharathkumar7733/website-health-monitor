import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)


SERVICENOW_INSTANCE = os.getenv("SERVICENOW_INSTANCE")
SERVICENOW_USERNAME = os.getenv("SERVICENOW_USERNAME")
SERVICENOW_PASSWORD = os.getenv("SERVICENOW_PASSWORD")


if not SERVICENOW_INSTANCE:
    raise ValueError("SERVICENOW_INSTANCE is missing from .env")

if not SERVICENOW_USERNAME:
    raise ValueError("SERVICENOW_USERNAME is missing from .env")

if not SERVICENOW_PASSWORD:
    raise ValueError("SERVICENOW_PASSWORD is missing from .env")
