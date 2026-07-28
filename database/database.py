import sqlite3
import os


# Database path

DB_PATH = "database/careerpilot.db"



def create_database():

    os.makedirs("database", exist_ok=True)


    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()



    # ---------------- USERS TABLE ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT,

        resume_name TEXT,

        ats_score REAL

    )
    """)



    # ---------------- SKILLS TABLE ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        category TEXT,

        skill TEXT,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)



    # ---------------- INTERVIEW RESULTS TABLE ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interview_results(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        score REAL,

        feedback TEXT,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)



    # ---------------- ROADMAP PROGRESS TABLE ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roadmap_progress(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        role TEXT,

        skill TEXT,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)



    # ---------------- ROLE ANALYSIS TABLE ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS role_analysis(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        role TEXT,

        score INTEGER,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)



    conn.commit()

    conn.close()


    print("CareerPilot AI Database Created Successfully!")



if __name__ == "__main__":

    create_database()