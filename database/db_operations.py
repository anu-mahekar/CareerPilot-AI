import sqlite3

DB_PATH = "database/careerpilot.db"


# ---------------- DATABASE CONNECTION ----------------

def get_connection():
    return sqlite3.connect(DB_PATH)



# ---------------- SAVE USER RESUME DETAILS ----------------

def save_user(name, email, resume_name, ats_score):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users(name,email,resume_name,ats_score)
    VALUES(?,?,?,?)
    """,
    (name, email, resume_name, ats_score))

    conn.commit()

    user_id = cursor.lastrowid

    print("USER SAVED:", user_id)

    conn.close()

    return user_id



# ---------------- GET LATEST USER ----------------

def get_latest_user():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id
    FROM users
    ORDER BY id DESC
    LIMIT 1
    """)

    result = cursor.fetchone()

    conn.close()


    if result:
        return result[0]

    return None



# ---------------- GET USER DETAILS ----------------

def get_user_details(user_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT name,email,resume_name,ats_score
    FROM users
    WHERE id=?
    """,
    (user_id,))


    result = cursor.fetchone()

    conn.close()


    if result:

        return {
            "name": result[0],
            "email": result[1],
            "resume_name": result[2],
            "ats_score": result[3]
        }


    return None



# ---------------- SAVE SKILLS ----------------

def save_skill(user_id, category, skill):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO skills(user_id,category,skill)
    VALUES(?,?,?)
    """,
    (user_id,category,skill))


    conn.commit()

    conn.close()



# ---------------- GET USER SKILLS ----------------

def get_user_skills(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, skill
    FROM skills
    WHERE user_id=?
    """,
    (user_id,))

    rows = cursor.fetchall()

    conn.close()

    skills = {}

    for category, skill in rows:

        if category not in skills:
            skills[category] = []

        skills[category].append(skill)

    return skills

# ---------------- SAVE ROLE MATCH ----------------

def save_role_match(user_id, role, score):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO role_analysis(user_id,role,score)
    VALUES(?,?,?)
    """,
    (user_id,role,score))


    conn.commit()

    conn.close()



# ---------------- GET ROLE MATCH ----------------

def get_role_match(user_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT role,score
    FROM role_analysis
    WHERE user_id=?
    ORDER BY id DESC
    LIMIT 1
    """,
    (user_id,))


    result = cursor.fetchone()

    conn.close()


    if result:

        return {
            "role":result[0],
            "score":result[1]
        }


    return {
        "role":"AI Engineer",
        "score":0
    }



# ---------------- SAVE ROADMAP PROGRESS ----------------

def save_roadmap_progress(user_id,role,skill):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO roadmap_progress(user_id,role,skill)
    VALUES(?,?,?)
    """,
    (user_id,role,skill))


    conn.commit()

    conn.close()



# ---------------- GET ROADMAP PROGRESS ----------------

def get_roadmap_progress(user_id,role):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT skill
    FROM roadmap_progress
    WHERE user_id=? AND role=?
    """,
    (user_id,role))


    result = cursor.fetchall()

    conn.close()


    return [row[0] for row in result]



# ---------------- GET ROADMAP PERCENTAGE ----------------

def get_roadmap_percentage(user_id,role,total_skills):

    completed = get_roadmap_progress(
        user_id,
        role
    )


    if total_skills == 0:
        return 0


    return int(
        (len(completed)/total_skills)*100
    )



# ---------------- SAVE INTERVIEW RESULT ----------------

def save_interview_result(user_id,score,feedback):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO interview_results(user_id,score,feedback)
    VALUES(?,?,?)
    """,
    (user_id,score,feedback))


    conn.commit()

    conn.close()



# ---------------- GET INTERVIEW PROGRESS ----------------

def get_interview_progress(user_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT COUNT(*)
    FROM interview_results
    WHERE user_id=?
    """,
    (user_id,))


    result = cursor.fetchone()

    conn.close()


    if result:

        completed = result[0]

        total_questions = 4


        return int(
            (completed/total_questions)*100
        )


    return 0

