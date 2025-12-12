import sqlite3

def fill_dummy_data():
    con = sqlite3.connect('school.db')
    cur = con.cursor()

    # 1. بيانات جدول Admin
    cur.execute("""
        INSERT INTO Admin (admin_name, admin_username, admin_password) 
        VALUES 
        ('Manager', 'admin', '12345'),
        ('Supervisor', 'super', 'admin123');
    """)

    # 2. بيانات جدول Account (المستخدمين)
    cur.execute("""
        INSERT INTO Account (name, username, password) 
        VALUES 
        ('Ahmed Ali', 'ahmed2024', 'pass123'),
        ('Sarah Taha', 'sarah_t', '567890');
    """)

    # 3. بيانات جدول Teachers (المعلمين)
    # لاحظ أننا أدخلنا البيانات الجديدة: national_id, salary, college_degree
    cur.execute("""
        INSERT INTO teachers (name, subject, phone, national_id, salary, college_degree) 
        VALUES 
        ('Mr. Ibrahim', 'Arabic', '01012345678', '29001011234567', '5000', 'Bachelor of Education'),
        ('Ms. Huda', 'Islamic', '01123456789', '29505051234567', '4500', 'Bachelor of Arts'),
        ('Mr. John', 'Math', '01234567890', '28810101234567', '6000', 'B.Sc Mathematics');
    """)

    # 4. بيانات جدول first_student (الطلاب)
    cur.execute("""
        INSERT INTO first_student (student_name, student_gender, student_age, address, contact, date, last_school, years_felid, health_problem, final_result) 
        VALUES 
        ('Mohamed Ahmed', 'Male', '10', 'Cairo, Nasr City', '01099887766', '12/09/2023', 'Future School', '0', 'None', 'Pass'),
        ('Fatima Hassan', 'Female', '11', 'Giza, Dokki', '01122334455', '15/09/2023', 'Sunrise School', '0', 'Asthma', 'Pass'),
        ('Omar Khaled', 'Male', '10', 'Alexandria', '01233445566', '10/09/2023', 'Nile School', '1', 'None', 'Fail');
    """)

    # 5. بيانات جدول islamic_marks (درجات التربية الإسلامية)
    cur.execute("""
        INSERT INTO islamic_marks (student_name, st_month, nd_month, chapter1, half_year, st_month1, nd_month2, chapter2, chapter3, final_exam, final_result) 
        VALUES 
        ('Mohamed Ahmed', '10', '9', '18', '45', '10', '10', '19', '20', '95', 'Excellent'),
        ('Fatima Hassan', '9', '9', '17', '40', '9', '8', '18', '19', '88', 'Very Good');
    """)

    # 6. بيانات جدول arabic_marks (درجات اللغة العربية)
    cur.execute("""
        INSERT INTO arabic_marks (student_name, st_month, nd_month, chapter1, half_year, st_month1, nd_month2, chapter2, chapter3, final_exam, final_result) 
        VALUES 
        ('Mohamed Ahmed', '10', '10', '20', '48', '10', '10', '20', '20', '98', 'Excellent'),
        ('Fatima Hassan', '8', '9', '15', '38', '9', '9', '16', '18', '85', 'Very Good');
    """)

    con.commit()
    con.close()
    print("Dummy data inserted successfully!")

if __name__ == "__main__":
    fill_dummy_data()