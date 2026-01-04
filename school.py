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
def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
    cursor.execute("DELETE FROM STUDENTS WHERE roll=%s", (roll,))
    db.commit()

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted successfully.")

def main(): #main body of the program -----1
  def main():
    while True:
        print("\n--- School Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
