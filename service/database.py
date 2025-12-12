import sqlite3
from service.decode import recreate_response

conn = sqlite3.connect("environment.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    hexData TEXT NOT NULL
)
""")
conn.commit()

    
def get_data_environment():
    cursor.execute("SELECT device, timestamp, hexData FROM sensor_data ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if not row:
        return {}
    return recreate_response(row[0], row[1], row[2])


def save_data(data):
    record = data["data"]
    cursor.execute(
        "INSERT INTO sensor_data (device, timestamp, hexData) VALUES (?, ?, ?)",
        (record["device"], record["timestamp"], record["hexData"])
    )
    conn.commit()
    
def get_data_history(limit=10):
    cursor.execute(f"SELECT device, timestamp, hexData FROM sensor_data ORDER BY id DESC LIMIT {limit}")
    rows = cursor.fetchall()
    
    last_update = [recreate_response(row[0], row[1], row[2]) for row in reversed(rows)]
    temperatures = [{"temp": entry["temperature"], "time": entry["timestamp"]} for entry in last_update]
    
    return temperatures
