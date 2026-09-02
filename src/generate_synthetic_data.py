from pathlib import Path
import pandas as pd
import numpy as np
from datetime import date, timedelta

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)

audiologists = pd.DataFrame([
    {"audiologist_id":"AUD001","display_name":"Audiologist 1","home_lat":53.3498,"home_lon":-6.2603,"active":1},
    {"audiologist_id":"AUD002","display_name":"Audiologist 2","home_lat":53.3890,"home_lon":-6.1450,"active":1},
    {"audiologist_id":"AUD003","display_name":"Audiologist 3","home_lat":53.2850,"home_lon":-6.2400,"active":1},
])

service_minutes = {
    "SERVICE": 60,
    "HEARING_TEST": 90,
    "FITTING": 60,
    "WAX_REMOVAL": 45,
}

start = date(2026, 9, 7)
types = list(service_minutes.keys())
rows = []
appointment_no = 1

for day_offset in range(10):
    d = start + timedelta(days=day_offset)
    if d.weekday() >= 5:
        continue
    for _, aud in audiologists.iterrows():
        count = int(rng.integers(3, 6))
        base_lat, base_lon = aud["home_lat"], aud["home_lon"]
        for _ in range(count):
            appt_type = rng.choice(types, p=[0.30, 0.35, 0.25, 0.10])
            lat = float(base_lat + rng.normal(0, 0.07))
            lon = float(base_lon + rng.normal(0, 0.10))
            rows.append({
                "appointment_id": f"APT{appointment_no:05d}",
                "appointment_date": d.isoformat(),
                "audiologist_id": aud["audiologist_id"],
                "patient_id": f"PAT{appointment_no:05d}",
                "appointment_type": appt_type,
                "planned_duration_min": service_minutes[appt_type],
                "appointment_lat": round(lat, 6),
                "appointment_lon": round(lon, 6),
                "status": "PLANNED"
            })
            appointment_no += 1

appointments = pd.DataFrame(rows)
audiologists.to_csv(RAW / "audiologists.csv", index=False)
appointments.to_csv(RAW / "appointments.csv", index=False)

print(f"Created {len(audiologists)} synthetic audiologists")
print(f"Created {len(appointments)} synthetic appointments")
print(f"Files saved to {RAW}")
