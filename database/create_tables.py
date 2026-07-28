import sqlite3


conn = sqlite3.connect("database/careerpilot.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS roadmap_progress(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER,

role TEXT,

skill TEXT

)
""")


conn.commit()

conn.close()


print("Roadmap table created successfully!")