import sqlite3
import csv
from datetime import date
# from main import User 

today = date.today()

con = sqlite3.connect("competency_tracker.db")
cur = con.cursor()


# with open("userdata.csv") as data:
#     csv_reader = csv.reader(data)
#     for i in csv_reader:
#         user = User(i[0],i[1],i[2],i[3],i[4],i[5])
#         user.create_user()


with open("competencies.csv") as comps:
    csv_reader = csv.reader(comps)
    for i in csv_reader:
        cur.execute("INSERT INTO Competencies (competency_name,date_added) VALUES (?,?)",(i[0],today))
        con.commit()


with open("assessments.csv") as tests:
    csv_reader = csv.reader(tests)
    for i in csv_reader:
        cur.execute("INSERT INTO Assessments (assessment_name,date_added) VALUES (?,?)",(i[0],today))
        con.commit()
