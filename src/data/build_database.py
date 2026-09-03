from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "data" / "audiology_analytics.db"

with sqlite3.connect(DB) as con:
    con.executescript((ROOT / "sql" / "schema.sql").read_text())
    for table, filename in [
        ("audiologists", "audiologists.csv"),
        ("appointments", "appointments.csv"),
    ]:
        df = pd.read_csv(ROOT / "data" / "raw" / filename)
        df.to_sql(table, con, if_exists="replace", index=False)

print(f"Database built: {DB}")
