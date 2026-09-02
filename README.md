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
