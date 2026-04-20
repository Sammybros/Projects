# Retail Inventory Forecasting Pipeline

A portfolio project designed to demonstrate practical **Data Engineering** skills using a retail and inventory use case.

## Project Goal
Build an end-to-end pipeline that ingests point-of-sale style sales data, transforms it into analytics-ready tables, loads it into a relational database, and supports simple demand forecasting.

This project aligns with common junior Data Engineer requirements:
- Python ETL development
- SQL schema design
- Data cleaning and transformation
- Basic forecasting workflow
- Business-facing analytics outputs

## Tech Stack
- Python
- Pandas
- PostgreSQL
- SQL
- Jupyter Notebook

## Project Structure
```text
retail-inventory-pipeline/
  data/
    sample_sales.csv
  notebooks/
    exploration.ipynb
  sql/
    schema.sql
    analytics_queries.sql
  src/
    ingest.py
    transform.py
    load.py
    forecast.py
  requirements.txt
  .gitignore
  README.md
```

## Pipeline Overview
1. **Ingest** raw sales and inventory data from CSV files.
2. **Transform** the data by cleaning nulls, standardizing date fields, and calculating derived metrics.
3. **Load** the cleaned data into PostgreSQL tables.
4. **Analyze** product-level and date-level trends through SQL queries.
5. **Forecast** future demand using a baseline time series method.

## Suggested Resume Bullets
- Built an end-to-end ETL pipeline to process retail sales and inventory data using Python and SQL.
- Designed a relational schema and analytics queries to support demand forecasting and stock planning.
- Automated data cleaning and loading workflows for business-ready reporting outputs.

## How to Run
1. Create a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Update database connection settings in `src/load.py`.
4. Run the scripts in order:
   - `python src/ingest.py`
   - `python src/transform.py`
   - `python src/load.py`
   - `python src/forecast.py`

## Future Enhancements
- Add Airflow orchestration
- Add Docker support
- Add cloud storage integration with AWS S3
- Add dbt models for transformations
- Replace baseline forecast with Prophet or XGBoost
