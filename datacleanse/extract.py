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

    def standardize_cols(cols: pd.Index) -> pd.Index:
        return (
            cols.str.strip()
            .str.lower()
            .str.replace(r"-", "_", regex=True)
            .str.replace(r"[^\w\s]", "", regex=True)
            .str.replace(r"\s+", "_", regex=True)
        )

    for file_path in unprocessed_dir.glob("*.*"):
        if file_path.suffix == ".csv":
            logger.info(f"Extracting CSV: {file_path.name}")
            df = pd.read_csv(file_path)
            df.columns = standardize_cols(df.columns)
            dataframes.append(df)
        elif file_path.suffix == ".json":
            logger.info(f"Extracting JSON: {file_path.name}")
            df = pd.read_json(file_path, orient="records")
            df.columns = standardize_cols(df.columns)
            dataframes.append(df)

    if not dataframes:
        logger.warning(f"No valid data files found in {unprocessed_dir}.")
        return pd.DataFrame()

    combined_df = pd.concat(dataframes, ignore_index=True)
    logger.info(f"Total raw rows extracted: {len(combined_df)}")
    return combined_df
