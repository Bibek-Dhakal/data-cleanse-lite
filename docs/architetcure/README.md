# Architecture

DataCleanse-Lite follows a modular Extract-Transform-Load (ETL) approach.

## Data Flow Diagram

```mermaid
graph TD
    A[Raw CSV/JSON] -->|Extract| B(Pandas DataFrame)
    B -->|Transform| C{Data Standardization}
    C -->|Imputation & Formatting| D[Validate using Pydantic]
    D -->|Pass| E[(SQLite Marts DB)]
    D -->|Fail| F[Quarantine Log CSV]
```

## Core Modules

- `extract.py`: Ingests payloads from `/unprocessed` safely without mutation.
- `transform.py`: Core `pandas` logic (deduplication, date parsing, text stripping).
- `validate.py`: Applies `pydantic` schema models to evaluate data integrity.
- `load.py`: Pushes valid records to relational `SQLAlchemy` engine and bad records to flat files.
