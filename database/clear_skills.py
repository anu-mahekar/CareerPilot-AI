import sqlite3


conn = sqlite3.connect("database/careerpilot.db")

cursor = conn.cursor()


cursor.execute("""
DELETE FROM skills
""")


conn.commit()

conn.close()


print("Old skills deleted")