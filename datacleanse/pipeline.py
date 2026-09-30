import logging
import time

from datacleanse import config
from datacleanse.extract import extract_raw_data
from datacleanse.load import load_marts, log_quarantine
from datacleanse.transform import clean_data
from datacleanse.validate import validate_and_split

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def run_pipeline():
    start_time = time.time()
    logger.info("Starting DataCleanse-Lite Pipeline...")

    # 1. Extract
    raw_df = extract_raw_data(config.RAW_DATA_DIR)
    if raw_df.empty:
        logger.info("Pipeline finished. No data to process.")
        return

    # 2. Transform
    cleaned_df = clean_data(raw_df)

    # 3. Validate
    valid_df, quarantine_df = validate_and_split(cleaned_df)

    # 4. Load
    load_marts(valid_df, config.DATABASE_URL)
    log_quarantine(quarantine_df, config.QUARANTINE_DIR)

    elapsed = time.time() - start_time
    logger.info(f"Pipeline Execution Complete in {elapsed:.2f} seconds.")
    logger.info(f"Summary -> Clean: {len(valid_df)} | Quarantined: {len(quarantine_df)}")


if __name__ == "__main__":
    run_pipeline()
