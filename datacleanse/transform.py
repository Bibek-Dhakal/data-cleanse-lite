import logging

import pandas as pd

logger = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies standardization, missing value imputation, and formatting.
    """
    if df.empty:
        return df

    initial_count = len(df)

    # Standardize column names to snake_case
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.replace(r"\s+", "_", regex=True)
    )

    # Required columns map to prevent KeyError on messy data
    required_cols = [
        "transaction_id",
        "customer_id",
        "product_id",
        "timestamp",
        "amount",
        "currency",
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = None

    # Deduplication
    df = df.drop_duplicates(subset=["transaction_id"], keep="first")
    logger.info(f"Dropped {initial_count - len(df)} duplicate transaction_ids.")

    # Impute missing numeric values
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["amount"] = df["amount"].fillna(0.0)

    # Standardize text
    df["currency"] = df["currency"].astype(str).str.upper().str.strip()
    df.loc[df["currency"].isin(["NAN", "NULL", "NONE"]), "currency"] = "USD"

    # Format dates safely
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Final text strip for string columns
    string_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip()

    return df
