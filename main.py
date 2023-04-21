from getpass import getpass
from datetime import date
import sqlite3
import csv
# import bcrypt


con = sqlite3.connect("competency_tracker.db")
cur = con.cursor()

def create_table(cursor):
    file = open("schema.sql")
    file_str = file.read()
    cursor.executescript(file_str)

result = create_table(cur)

today = date.today()

class User:
    
    def __init__(self, f_name, l_name, phone, email, password, hire):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.email = email
        self.password = password
        self.hire_date = hire

    def create_user(self):
        self.date_created = today
        cur.execute("INSERT INTO Users (first_name,last_name,phone,email,password,hire_date,date_created) VALUES (?,?,?,?,?,?,?)", (self.f_name, self.l_name, self.phone, self.email, self.password, self.hire_date, self.date_created)).fetchall();
        con.commit()

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

# print(get_average(1))

def user_home_page():
    pass

def manager_home_page():
    pass


# user1 = User("Lacey","Sanabria","3857750556","laceysanabria@outlook.com","C0dingMaster\^o^/","2021-04-16")
# User.create_user(user1)



while True:
    print("\n\t~~COMPETENCY TRACKER~~\n\nPlease log in:\n")
    username_input = input("Email: ")
    password_input = getpass("Password: ")

    if check_login(username_input,password_input):
        #if user_type == manager -> manager_home_page()
        #else -> user_home_page()
        pass
    elif username_input.lower() == "q" or password_input.lower() == "q":
        quit()
    else:
        print("The email or password you entered is incorrect.")
        continue

