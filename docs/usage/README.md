# Usage & Configuration

## Environment Variables

| Name             | Type   | Default Value                       | Description                               |
|------------------|--------|-------------------------------------|-------------------------------------------|
| `DATABASE_URL`   | String | `sqlite:///data/processed/marts.db` | SQLAlchemy connection string for SQLite.  |
| `RAW_DATA_DIR`   | String | `data/unprocessed`                  | Directory to poll for raw JSON/CSV data.  |
| `QUARANTINE_DIR` | String | `data/quarantine`                   | Path to output failed records log.        |
| `PROCESSED_DIR`  | String | `data/processed`                    | Path for SQLite DB output.                |
| `BATCH_SIZE`     | Int    | `10000`                             | Chunking size for loading data if needed. |

## Available Commands

- **Generate Data:** `python scripts/generate_sample_data.py`
- **Run Pipeline:** `python -m datacleanse.pipeline`
- **Run Notebook:** `jupyter notebook notebooks/Data_Exploration_and_Cleaning.ipynb`
