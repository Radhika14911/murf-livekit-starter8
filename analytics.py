import sqlite3

conn = sqlite3.connect("call_analytics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS calls(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    outcome TEXT
)
""")

conn.commit()

def save_call(outcome):
    cursor.execute(
        "INSERT INTO calls(outcome) VALUES(?)",
        (outcome,)
    )
    conn.commit()

print("Analytics DB Ready")

save_call("success")
save_call("success")
save_call("failed")