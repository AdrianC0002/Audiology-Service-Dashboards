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

## Source Code Organisation

The Python source code is divided into separate modules based on responsibility.

### Data Module

The `src/data/` package contains the project's data-engineering components:

- `generate_synthetic_data.py` generates synthetic audiologist and appointment data for development and testing.
- `build_database.py` loads the generated datasets into the local SQLite analytics database.

Project paths are resolved relative to the repository root so that the project can be cloned and run on different computers without hard-coded local paths.

### Routing Module

The `src/routing/` package contains the geographic routing and optimisation components:

- `routing_google.py` provides the foundation for road travel-time and road-distance calculations.
- `route_optimizer.py` provides the initial Google OR-Tools route optimisation logic.

The routing system will eventually support:

- Audiologist home-to-first-appointment travel.
- Appointment-to-appointment travel.
- Final appointment-to-home travel.
- Individual audiologist daily route optimisation.
- Appointment service durations.
- Appointment time windows.
- Working-hour and break constraints.
- Scheduling conflict detection.
- Company-wide daily route optimisation across all available audiologists and appointments.
- Comparison of current routes against recommended fastest routes.
- Estimated driving-time and distance savings.

## Machine Learning and Testing Environment

The project includes a dedicated machine learning and automated testing environment.

### Machine Learning Stack

The machine learning stack currently includes:

- `scikit-learn` for preprocessing, baseline models, classification, regression and model evaluation.
- `XGBoost` for advanced predictive modelling.
- `joblib` for saving trained machine learning models.
- `matplotlib` for model evaluation and analytical visualisations.

Four machine learning components are planned.

#### 1. Appointment Demand Forecasting

Forecast future demand for hearing tests, fittings, services, wax-removal appointments and other appointment types.

The model will support workforce capacity planning and geographic demand analysis.

#### 2. Cancellation and No-Show Prediction

Estimate the probability that an appointment will be cancelled or missed.

Predictions are intended for operational planning and reminder support rather than clinical decision-making.

#### 3. Helpdesk Issue Classification

Use natural language processing to automatically classify synthetic helpdesk messages into categories such as:

- Bluetooth and connectivity
- Charging
- Batteries
- Mobile application issues
- Streaming
- Cleaning
- Wax filters
- Receivers
- Feedback or whistling
- Repairs
- Appointment queries

#### 4. Inventory Demand Forecasting

Forecast future demand for frequently used audiology accessories and parts such as domes, wax filters, receivers, batteries and chargers.

### Automated Testing

The project uses `pytest` for automated testing and `pytest-cov` for code-coverage measurement.

The initial automated test suite verifies that:

- The Python testing environment is operational.
- scikit-learn can be imported successfully.
- XGBoost can be imported successfully.
- Google OR-Tools can be imported successfully.

Future tests will cover data validation, database operations, appointment rules, route optimisation, scheduling logic and machine learning preprocessing.

## Operational Business Rules

Operational settings are stored centrally in `config/business_rules.json`.

This allows appointment durations, working hours, travel buffers and route optimisation settings to be changed without modifying the core Python code.

### Appointment Durations

| Appointment Type | Duration |
|---|---:|
| Service | 60 minutes |
| Hearing Test | 90 minutes |
| Fitting | 60 minutes |
| Wax Removal | 45 minutes (prototype assumption) |

The wax-removal duration will be updated when the standard business appointment length is confirmed.

### Working Day

The current prototype assumes:

- Working day starts at 08:30.
- Working day ends at 17:30.
- 30-minute lunch break.
- 10-minute travel buffer between journeys.

These settings are configurable.

### Individual Route Optimisation

The individual routing mode keeps appointments assigned to their existing audiologist and searches for the fastest feasible daily sequence.

Each route starts from the audiologist's home location and returns to the home location after the final appointment.

### Company-Wide Daily Route Optimisation

The platform will also support a company-wide optimisation mode.

For a selected day, the system will consider all available audiologists and all home appointments simultaneously.

The optimisation engine will recommend:

- Which audiologist should attend each appointment.
- The recommended appointment sequence for each audiologist.
- Departure and arrival times.
- Total driving time.
- Total driving distance.
- Estimated return-home time.
- Scheduling conflicts.
- Overtime risk.
- Estimated travel-time savings.
- Estimated distance savings.

The optimisation will respect:

- Appointment times.
- Appointment duration.
- Audiologist availability.
- Required audiologist skills.
- Working-hour constraints.
- Travel buffers.
- Home starting locations.
- Home return locations.

The objective is to reduce unnecessary travel while maintaining feasible appointment schedules.

### Machine Learning Configuration

The project configuration enables four planned machine learning components:

1. Appointment demand forecasting.
2. Cancellation and no-show prediction.
3. Helpdesk issue classification.
4. Inventory demand forecasting.

Automated tests verify that key business rules remain correctly configured.