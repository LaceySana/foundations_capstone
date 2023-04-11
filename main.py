from getpass import getpass
from datetime import date
import sqlite3
# import bcrypt


con = sqlite3.connect("competency_tracker.db")
cur = con.cursor()

def create_table(cursor):
    file = open("schema.sql")
    file_str = file.read()
    cursor.executescript(file_str)

result = create_table(cur)

class User():
    pass

def check_login(uname,pword):
    pass

def view_users():
    pass

def search_user():
    pass

def view_report_for_competency():
    pass

def view_report_for_user():
    pass

def view_assessments_for_user():
    pass

def add():
    pass

def edit():
    pass

def delete_result():
    pass

def export_csv():
    pass

def import_csv():
    pass

def get_average(user_id):
    scores = cur.execute("SELECT score FROM Assessment_Results").fetchall();
    scores = list(scores)
    average = 0
    for i in scores:
        average += i
    return average
    

def user_home_page():
    pass

def manager_home_page():
    pass


while True:
    print("\n\t~~COMPETENCY TRACKER~~\n\nPlease log in:\n")
    username_input = input("Email: ")
    password_input = getpass("Password: ")

    if check_login(username_input,password_input):
        #if user_type == manager -> manager_home_page()
        #else -> user_home_page()
        pass
    else:
        print("The email or password you entered is incorrect.")
        continue