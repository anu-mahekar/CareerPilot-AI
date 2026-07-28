import sqlite3


conn = sqlite3.connect("database/careerpilot.db")

cursor = conn.cursor()


cursor.execute("""
ALTER TABLE skills
ADD COLUMN category TEXT
""")


conn.commit()

conn.close()


print("Category column added successfully!")