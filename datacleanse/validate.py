from datetime import datetime

import pandas as pd
from pydantic import BaseModel, Field, ValidationError


class TransactionSchema(BaseModel):
    transaction_id: str = Field(..., min_length=1)
    customer_id: str = Field(..., min_length=1)
    product_id: str = Field(..., min_length=1)
    timestamp: datetime
    amount: float
    currency: str = Field(..., min_length=3, max_length=3)


def validate_and_split(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Validates rows against Pydantic schema.
    Returns (valid_df, quarantined_df).
    """
    valid_records = []
    quarantined_records = []

    # Iterate as dicts for fast pydantic validation
    records = df.to_dict(orient="records")

    for record in records:
        # Filter out literal 'nan' strings caused by pandas string conversion
        clean_record = {
            k: (None if str(v).lower() in ("nan", "nat", "<na>") else v) for k, v in record.items()
        }

        try:
            valid_txn = TransactionSchema(**clean_record)
            valid_records.append(valid_txn.model_dump())
        except ValidationError as e:
            clean_record["quarantine_reason"] = str(e).replace("\n", "; ")
            quarantined_records.append(clean_record)

    valid_df = pd.DataFrame(valid_records)
    quarantine_df = pd.DataFrame(quarantined_records)

    return valid_df, quarantine_df
