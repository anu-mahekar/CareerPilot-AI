import sqlite3

DB_PATH = "database/careerpilot.db"


def create_database():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        resume_name TEXT,
        ats_score REAL
    )
    """)


    # Skills table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        skill TEXT
    )
    """)


    # Role analysis table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS role_analysis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT,
        score INTEGER
    )
    """)


    # Roadmap progress table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roadmap_progress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT,
        skill TEXT
    )
    """)


    # Interview results table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interview_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        score REAL,
        feedback TEXT
    )
    """)


    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")