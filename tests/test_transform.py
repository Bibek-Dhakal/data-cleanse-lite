import pandas as pd

from datacleanse.transform import clean_data


def test_clean_data_standardizes_columns():
    df = pd.DataFrame(
        {
            "Transaction ID ": ["1"],
            "CUSTOMER_ID": ["C1"],
            "product-id": ["P1"],
            "timestamp": ["2023-01-01"],
            "Amount": [100.0],
            "currency": ["USD"],
        }
    )

    cleaned = clean_data(df)
    expected_cols = [
        "transaction_id",
        "customer_id",
        "product_id",
        "timestamp",
        "amount",
        "currency",
    ]

    assert list(cleaned.columns) == expected_cols


def test_clean_data_handles_missing_amount():
    df = pd.DataFrame({"transaction_id": ["1", "2"], "amount": [100.0, None]})
    cleaned = clean_data(df)

    assert cleaned.iloc[0]["amount"] == 100.0
    assert cleaned.iloc[1]["amount"] == 0.0


def test_clean_data_removes_duplicates():
    df = pd.DataFrame({"transaction_id": ["1", "1", "2"]})
    cleaned = clean_data(df)
    assert len(cleaned) == 2
