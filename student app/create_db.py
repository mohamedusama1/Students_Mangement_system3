import sqlite3

def create_db():
    con = sqlite3.connect('school.db')
    cur = con.cursor()

    # --- Account table ---
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Account(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT,
            password TEXT
        )
    """)

    # --- Admin table ---
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Admin(
            admin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_name TEXT,
            admin_username TEXT,
            admin_password TEXT
        )
    """)

    # --- Student table ---
    cur.execute("""
        CREATE TABLE IF NOT EXISTS first_student(
            s_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            student_gender TEXT,
            student_age TEXT,
            address TEXT,
            contact TEXT,
            date TEXT,
            last_school TEXT,
            years_felid TEXT,
            health_problem TEXT,
            final_result TEXT
        )
    """)

    # --- Islamic Marks table ---
    cur.execute("""
        CREATE TABLE IF NOT EXISTS islamic_marks(
            i_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            st_month TEXT,
            nd_month TEXT,
            chapter1 TEXT,
            half_year TEXT,
            st_month1 TEXT,
            nd_month2 TEXT,
            chapter2 TEXT,
            chapter3 TEXT,
            final_exam TEXT,
            final_result TEXT
        )
    """)

    # --- Arabic Marks table ---
    cur.execute("""
        CREATE TABLE IF NOT EXISTS arabic_marks(
            a_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            st_month TEXT,
            nd_month TEXT,
            chapter1 TEXT,
            half_year TEXT,
            st_month1 TEXT,
            nd_month2 TEXT,
            chapter2 TEXT,
            chapter3 TEXT,
            final_exam TEXT,
            final_result TEXT
        )
    """)

    # --- Teachers table ---
    # Note: Added national_id, salary, and college_degree columns
    cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            t_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            subject TEXT,
            phone TEXT,
            national_id TEXT,
            salary TEXT,
            college_degree TEXT
        )
    """)

    con.commit()
    con.close()
    print("Database created successfully.")

if __name__ == "__main__":
    create_db()