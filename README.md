# DataCleanse-Lite

**Automated Multi-Source E-Commerce ETL Pipeline with Pandas Data Cleaning, Validation Checks, and SQL Storage**

## Overview

Raw data collected from disparate channels (marketing APIs, e-commerce web dumps, customer feedback forms) is
unstandardized, contains duplicates, missing fields, and corrupt formats. `DataCleanse-Lite` is an automated,
lightweight ETL pipeline that processes messy CSV and JSON files, cleans them using `pandas`, validates constraints
using `pydantic`, and loads the normalized data into a relational SQLite schema.

### Core Features

- **Data Standardization:** Handles missing values, strips invalid characters, and formats dates.
- **Strict Validation:** Asserts null constraints, data types, and uniqueness.
- **Quarantine System:** Bad records are gracefully logged to quarantine files rather than silently dropped.
- **High Throughput:** Designed to process 100,000 messy records in under 30 seconds using in-memory `pandas`
  manipulation.

## Documentation Index

- [Architecture & Design](docs/architecture/README.md)
- [Usage & Configuration](docs/usage/README.md)
- [Testing Strategy](docs/testing/README.md)
- [Code Quality Standards](docs/code_quality.md)
- [Run Results & Performance Metrics](docs/results/README.md)

## Quickstart

1. **Install dependencies:**
   ```bash
   pip install -e .[dev,test]
   ```
2. **Setup environment:**
   ```bash
   cp .env.example .env
   ```
3. **Generate Sample Messy Data:**
   ```bash
   python scripts/generate_sample_data.py
   ```
4. **Run the ETL Pipeline:**
   ```bash
   python -m datacleanse.pipeline
   ```
