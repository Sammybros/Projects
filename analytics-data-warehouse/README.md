# Analytics Data Warehouse

A portfolio project designed to demonstrate practical **Data Engineering** and **SQL** skills through dimensional modeling and analytics reporting.

## Functional Outcomes (Aligned to Resume Impact)
This project simulates business reporting infrastructure that supports operational and analytical decision-making.

### Key Results Demonstrated
- Centralized raw transactional data into analytics-ready fact and dimension tables
- Improved reporting efficiency by enabling reusable SQL queries for KPI tracking
- Reduced manual spreadsheet-style reporting effort through structured warehouse design
- Strengthened SQL proficiency with joins, aggregations, and window-function style reporting patterns

## Project Goal
Design a simple analytics warehouse using a star schema to support business reporting for retail sales and inventory-related insights.

## Tech Stack
- SQL
- PostgreSQL
- Python (optional loader)
- CSV sample data

## Project Structure
```text
analytics-data-warehouse/
  data/
    products.csv
    sales.csv
  sql/
    create_tables.sql
    load_sample_data.sql
    business_queries.sql
  src/
    load_csv_to_postgres.py
  README.md
```

## Warehouse Design
### Fact Table
- `fact_sales`

### Dimension Tables
- `dim_product`
- `dim_date`

## Reporting Use Cases
- Total sales by day
- Sales by product category
- Top-selling products
- Monthly revenue trends
- Inventory planning support

## Resume Mapping Example
- Designed a dimensional data warehouse to support business reporting and KPI analysis
- Wrote SQL transformations and analytical queries using joins and aggregations
- Improved reporting consistency through structured fact and dimension models

## How to Run
1. Create the tables from `sql/create_tables.sql`
2. Load sample data from `sql/load_sample_data.sql` or use `src/load_csv_to_postgres.py`
3. Run analytical queries from `sql/business_queries.sql`

## Future Enhancements
- Add dbt models
- Add Airflow orchestration
- Add cloud warehouse migration to BigQuery or Redshift
- Add dashboard layer for reporting consumption
