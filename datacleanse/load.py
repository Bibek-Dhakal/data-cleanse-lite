import logging
from datetime import datetime
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


def load_marts(df: pd.DataFrame, db_url: str, table_name: str = "fact_sales") -> None:
    """
    Loads validated data into the target SQL database schema.
    """
    if df.empty:
        logger.info("No valid records to load into database.")
        return

    engine = create_engine(db_url)

    df.to_sql(table_name, con=engine, if_exists="append", index=False)
    logger.info(f"Successfully loaded {len(df)} records into '{table_name}'.")


def log_quarantine(df: pd.DataFrame, quarantine_dir: Path) -> None:
    """
    Saves bad records to a CSV log with error reasons.
    """
    if df.empty:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = quarantine_dir / f"quarantine_{timestamp}.csv"

    df.to_csv(file_path, index=False)
    logger.warning(f"Quarantined {len(df)} records. Saved to {file_path}")
