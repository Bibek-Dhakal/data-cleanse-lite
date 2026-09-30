import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/data/processed/marts.db")
RAW_DATA_DIR = Path(os.getenv("RAW_DATA_DIR", BASE_DIR / "data" / "unprocessed"))
QUARANTINE_DIR = Path(os.getenv("QUARANTINE_DIR", BASE_DIR / "data" / "quarantine"))
PROCESSED_DIR = Path(os.getenv("PROCESSED_DIR", BASE_DIR / "data" / "processed"))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "10000"))

# Ensure directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
QUARANTINE_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
