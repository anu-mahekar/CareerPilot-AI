import sqlite3


conn = sqlite3.connect("database/careerpilot.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS role_analysis(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    role TEXT,

    score INTEGER

)
""")


conn.commit()

conn.close()


print("Role analysis table created successfully!")