import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="1234567890",database="school_db")
#connecting to my database by entering my details 

cursor= db.cursor()

def add_student(): #created my own function to add a new student
  roll= int(input("Enter Roll no:"))
  name= imput("Enter Name:")
  age= int(input("Enter Age:"))
  grade= imput("Enter Class:")

query="INSERT INTO STUDENTS VALUES(%s, %s, %s, %s)"
values=(roll,name,age,grade)

try: #error handeling 
  cursor.execute(query,values)
  db.commit()
  print("Student Added Suscessfully.")
except:
  print("Student already exist with this Roll No.")
