import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "business_rules.json"


def load_business_rules():
    """Load operational business rules from the project configuration."""

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    rules = load_business_rules()

    print("Business rules loaded successfully.")
    print(
        "Hearing test duration:",
        rules["appointment_durations_minutes"]["HEARING_TEST"],
        "minutes",
    )
    print(
        "Company-wide optimisation:",
        rules["routing"]["company_wide_daily_optimisation"],
    )