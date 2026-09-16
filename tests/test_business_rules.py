from src.data.config_loader import load_business_rules


def test_business_rules_load():
    """Business rules configuration should load successfully."""

    rules = load_business_rules()

    assert rules is not None


def test_hearing_test_duration():
    """Hearing tests should currently be configured for 90 minutes."""

    rules = load_business_rules()

    assert rules["appointment_durations_minutes"]["HEARING_TEST"] == 90


def test_service_duration():
    """Service appointments should currently be configured for 60 minutes."""

    rules = load_business_rules()

    assert rules["appointment_durations_minutes"]["SERVICE"] == 60


def test_fitting_duration():
    """Fitting appointments should currently be configured for 60 minutes."""

    rules = load_business_rules()

    assert rules["appointment_durations_minutes"]["FITTING"] == 60


def test_route_starts_and_ends_at_home():
    """Audiologist routes should begin and finish at home."""

    rules = load_business_rules()

    assert rules["routing"]["start_from_home"] is True
    assert rules["routing"]["return_home"] is True


def test_company_wide_optimisation_enabled():
    """The full daily multi-audiologist optimiser should be enabled."""

    rules = load_business_rules()

    assert rules["routing"]["company_wide_daily_optimisation"] is True


def test_machine_learning_models_enabled():
    """All four planned ML components should be enabled."""

    rules = load_business_rules()
    ml = rules["machine_learning"]

    assert ml["appointment_demand_forecasting"] is True
    assert ml["cancellation_no_show_prediction"] is True
    assert ml["helpdesk_issue_classification"] is True
    assert ml["inventory_demand_forecasting"] is True