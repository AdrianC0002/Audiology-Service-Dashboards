# Audiology Service Insights Platform — Starter

Synthetic prototype for an integrated audiology operations analytics system.

## First modules
- Appointments
- Audiologist geographic routing
- Helpdesk
- Devices
- Repairs
- Feedback
- Executive reporting

## Privacy rule
Use synthetic data until management / IT / data-protection approval is obtained.
Never put real patient information, patient addresses, audiologist home addresses,
or API credentials in a personal GitHub repository.

## Run on Windows

1. Open the folder in VS Code.
2. Open Terminal > New Terminal.
3. Run:
   python -m venv .venv
4. Activate:
   .venv\Scripts\activate
5. Install:
   pip install -r requirements.txt
6. Generate fake data:
   python src\generate_synthetic_data.py
7. Build the SQLite database:
   python src\build_database.py

Database output:
data\audiology_analytics.db

## Routing design

For each audiologist and each working day:

HOME -> Appointment 1 -> Appointment 2 -> ... -> HOME

The system obtains actual road travel time/distance from an approved routing provider,
then OR-Tools selects a practical sequence while respecting appointment durations and,
in the full version, booked time windows and breaks.

## Project Structure

Audiology-Service-Dashboards uses a modular project structure designed to support data engineering, business analytics, geographic route optimisation, machine learning and Power BI reporting.

### Main Directories

- `config/` - Business rules and system configuration.
- `data/raw/` - Locally generated raw synthetic data.
- `data/processed/` - Cleaned and transformed analytical data.
- `data/sample/` - Small synthetic datasets that can safely be included in the public portfolio.
- `docs/` - Project documentation and data dictionaries.
- `models/` - Machine learning model outputs.
- `notebooks/` - Exploratory analysis and machine learning development.
- `outputs/predictions/` - Generated machine learning predictions.
- `outputs/reports/` - Generated analytical reports.
- `outputs/routes/` - Individual and company-wide route optimisation results.
- `powerbi/` - Power BI dashboards and supporting documentation.
- `sql/` - Database schemas, SQL queries and analytical views.
- `src/data/` - Data generation, cleaning and database processing.
- `src/analytics/` - Business analytics and KPI calculations.
- `src/routing/` - Geographic routing and optimisation.
- `src/ml/` - Machine learning pipelines.
- `tests/` - Automated project tests.

### Planned Analytics Platform

The completed platform will include:

- Appointment and service analytics.
- Audiologist workload and capacity analysis.
- Home-visit geographic analysis.
- Individual audiologist daily route optimisation.
- Company-wide daily route optimisation across all available audiologists and appointments.
- Helpdesk analytics.
- Device, fitting, repair and aftercare analysis.
- Customer journey analysis.
- Inventory analytics.
- Data-quality monitoring.
- Power BI management dashboards.
- Appointment demand forecasting.
- Cancellation and no-show prediction.
- Helpdesk issue text classification.
- Inventory demand forecasting.