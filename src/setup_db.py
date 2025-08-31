
import sqlite3
import os

os.makedirs("data", exist_ok=True)
DB_PATH = "data/INFO.db"

# Create table
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS info (
    PLATE TEXT PRIMARY KEY,
    OWNER TEXT,
    CONTACT TEXT,
    MODEL TEXT
)
""")

# Insert demo records
cars = [
    ("plate_number_1", "owner_1", "contact_number_1", "car_model_1"),
    ("plate_number_2", "owner_2", "contact_number_2", "car_model_2"),
    ("plate_number_3", "owner_3", "contact_number_3", "car_model_3")
]

c.executemany("INSERT OR REPLACE INTO info VALUES (?, ?, ?, ?)", cars)
conn.commit()
conn.close()

print("✅ Demo DB created at data/INFO.db")
