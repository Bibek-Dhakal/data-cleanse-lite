import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def extract_raw_data(unprocessed_dir: Path) -> pd.DataFrame:
    """
    Reads all JSON and CSV files from the unprocessed directory
    and concatenates them into a single pandas DataFrame.
    Original files remain untouched.
    """
    dataframes = []

    for file_path in unprocessed_dir.glob("*.*"):
        if file_path.suffix == ".csv":
            logger.info(f"Extracting CSV: {file_path.name}")
            df = pd.read_csv(file_path)
            dataframes.append(df)
        elif file_path.suffix == ".json":
            logger.info(f"Extracting JSON: {file_path.name}")
            df = pd.read_json(file_path, orient="records")
            dataframes.append(df)

    if not dataframes:
        logger.warning(f"No valid data files found in {unprocessed_dir}.")
        return pd.DataFrame()

    combined_df = pd.concat(dataframes, ignore_index=True)
    logger.info(f"Total raw rows extracted: {len(combined_df)}")
    return combined_df
