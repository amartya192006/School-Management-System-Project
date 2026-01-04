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

def edit_student(): #2nd function 
  roll = int(input("Enter Roll Number to edit: "))
  name = input("Enter New Name: ")
  age = int(input("Enter New Age: "))
  grade = input("Enter New Grade: ")
  query= """
  UPDATE STUDENTS SET name=%s, age=%s, grade=%s WHERE roll=%s """
  cursor.execute(query,(name,age,grade,roll))
  db.commit()
  if cursor.rowcount ==0:
    print("STUDENT LIST IS EMPTY")
  else:
    print("Student Details Updated")



