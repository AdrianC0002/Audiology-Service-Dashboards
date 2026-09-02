PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS audiologists (
    audiologist_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    home_lat REAL,
    home_lon REAL,
    active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id TEXT PRIMARY KEY,
    appointment_date TEXT NOT NULL,
    audiologist_id TEXT NOT NULL,
    patient_id TEXT NOT NULL,
    appointment_type TEXT NOT NULL,
    planned_duration_min INTEGER NOT NULL,
    appointment_lat REAL,
    appointment_lon REAL,
    status TEXT NOT NULL,
    scheduled_start TEXT,
    scheduled_end TEXT,
    FOREIGN KEY (audiologist_id) REFERENCES audiologists(audiologist_id)
);

CREATE TABLE IF NOT EXISTS route_legs (
    route_leg_id TEXT PRIMARY KEY,
    route_date TEXT NOT NULL,
    audiologist_id TEXT NOT NULL,
    leg_sequence INTEGER NOT NULL,
    origin_type TEXT NOT NULL,
    origin_ref TEXT NOT NULL,
    destination_type TEXT NOT NULL,
    destination_ref TEXT NOT NULL,
    distance_km REAL,
    drive_duration_min REAL,
    traffic_duration_min REAL,
    planned_departure TEXT,
    planned_arrival TEXT,
    FOREIGN KEY (audiologist_id) REFERENCES audiologists(audiologist_id)
);

CREATE TABLE IF NOT EXISTS helpdesk_cases (
    case_id TEXT PRIMARY KEY,
    opened_at TEXT NOT NULL,
    patient_id TEXT,
    issue_category TEXT NOT NULL,
    device_brand TEXT,
    device_model TEXT,
    resolution_minutes INTEGER,
    first_contact_resolved INTEGER,
    escalated INTEGER,
    follow_up_required INTEGER
);

CREATE TABLE IF NOT EXISTS devices (
    device_id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    brand TEXT,
    model TEXT,
    fitted_date TEXT
);

CREATE TABLE IF NOT EXISTS repairs (
    repair_id TEXT PRIMARY KEY,
    device_id TEXT NOT NULL,
    reported_date TEXT,
    returned_date TEXT,
    reason TEXT,
    status TEXT,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

CREATE TABLE IF NOT EXISTS feedback (
    feedback_id TEXT PRIMARY KEY,
    patient_id TEXT,
    submitted_date TEXT,
    service_type TEXT,
    score INTEGER,
    comment TEXT
);
