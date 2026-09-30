import csv
import json
import os
import random
import uuid
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNPROCESSED_DIR = os.path.join(BASE_DIR, "data", "unprocessed")


def generate_messy_data(num_rows=100000):
    os.makedirs(UNPROCESSED_DIR, exist_ok=True)

    csv_file = os.path.join(UNPROCESSED_DIR, "sales_dump_1.csv")
    json_file = os.path.join(UNPROCESSED_DIR, "api_payload_1.json")

    csv_data = []
    json_data = []

    print(f"Generating {num_rows} messy records...")

    for i in range(num_rows):
        # Introduce duplicates occasionally
        txn_id = str(uuid.uuid4()) if random.random() > 0.05 else "DUPLICATE_TXN_001"

        row = {
            "Transaction ID ": txn_id,  # Messy column name handled in pandas
            "CUSTOMER_ID": f"CUST_{random.randint(1000, 9999)}" if random.random() > 0.01 else None,
            "product-id": f"PROD_{random.randint(10, 99)}",
            "timestamp ": (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
            if random.random() > 0.02
            else "INVALID_DATE",
            "Amount": round(random.uniform(5.0, 500.0), 2)
            if random.random() > 0.05
            else None,  # Missing amounts
            "currency": random.choice(["USD", "usd", " EUR ", "GBP", ""]),
        }

        if i % 2 == 0:
            csv_data.append(row)
        else:
            # Snake case variations for JSON to simulate disparate sources
            json_data.append(
                {
                    "transaction_id": row["Transaction ID "],
                    "customer_id": row["CUSTOMER_ID"],
                    "product_id": row["product-id"],
                    "timestamp": row["timestamp "],
                    "amount": row["Amount"],
                    "currency": row["currency"],
                }
            )

    # Write CSV
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "Transaction ID ",
                "CUSTOMER_ID",
                "product-id",
                "timestamp ",
                "Amount",
                "currency",
            ],
        )
        writer.writeheader()
        writer.writerows(csv_data)

    # Write JSON
    with open(json_file, "w") as f:
        json.dump(json_data, f, indent=2)

    print(f"Done! Created {csv_file} and {json_file}")


if __name__ == "__main__":
    generate_messy_data(100000)
