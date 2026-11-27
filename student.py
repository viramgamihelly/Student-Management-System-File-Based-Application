# Function	Responsibility
# add_student()	Add a new student
# view_students()	Display all students
# search_student()	Find student by roll number
# update_student()	Update existing student details
# delete_student()	Delete a student
# calculate_average()	Calculate average marks
# students_above_75()   Display students scoring above 75

# [name,roll,course,marks]
from decorators import log_activity
from validators import validate_marks,InvalidMarksError
from file_handler import read_students, filtered_students_above_75, filename
import csv

# filename=r"C:\Users\Dell\Documents\CLG NOTESSSSSSS\EXTRA\week4-project\data\student.csv"

@log_activity
def add_student():
    num=int(input("Enter the number of students to add: "))

    for i in range(num):
        name=input("Enter Student name: ").capitalize()
        roll=input("Enter Student roll number: ")
        course=input("Enter Student course: ").capitalize()
        while True:
            try:
                marks = validate_marks(input("Enter Student marks (0-100): "))
                break

            except InvalidMarksError as e:
                print(e)
                print("Please enter marks again.")

        exists=False

        try:
            with open(filename,"r",newline="") as file:
                read=csv.reader(file)
                for row in read:
                    if row[1]==roll:
                        exists=True
                        break
        except FileNotFoundError:
            exists=False

        if exists:
            print("Student with this roll number already exists!")
            continue

        with open(filename,"a",newline="") as file:
            write=csv.writer(file)

            write.writerow([name,roll,course,marks])

        print(f"Student {name} added")

    print("Data saved !")
    print("-"*30)

@log_activity
def view_students():
    print("\t---DISPLAYING STUDENT DETAILS---")

    found = False

    print(f"{'Name':<30}{'Roll No':<15}{'Course':<30}{'Marks':<10}")

    for row in read_students():
        found = True
        print(f"{row[0]:<30}{row[1]:<15}{row[2]:<30}{row[3]:<10}")

    if not found:
        print("No student records found!")

    print("-" * 100)

@log_activity
def search_student():
    roll = input("Enter Student roll number to search: ")

    found = False

    for row in read_students():
        if row[1] == roll:
            found = True
            print("Student found!")
            print("Student details:")
            print(f"Name: {row[0]}")
            print(f"Roll Number: {row[1]}")
            print(f"Course: {row[2]}")
            print(f"Marks: {row[3]}")
            break

    if not found:
        print(f"Student having roll number {roll} not found!")

@log_activity
def update_student():
    roll=input("Enter the student roll number you want to update: ")
    exists=False
    update=[]

    for row in read_students():
        if row[1]==roll:
            exists=True
            print("update the details here:")
            name=input("Enter Student name: ").capitalize()
            course=input("Enter Student Course: ").capitalize()
            while True:
                try:
                    marks = validate_marks(input("Enter Student marks (0-100): "))
                    break

                except InvalidMarksError as e:
                    print(e)
                    print("Please enter marks again.")
            row[0]=name
            row[2]=course
            row[3]=marks
        update.append(row)

    if exists:
        with open(filename,"w",newline="") as file:
            write=csv.writer(file)
            write.writerows(update)

            print("Details updated!")
    else:
        print("student not found!")

@log_activity
def delete_student():
    roll=input("Enter the roll number you want to delete: ")
    choice=input("Are you sure you want to delete Student(Yes/No)? : ").strip().capitalize()
    exists=False
    updated=[]
    if choice=="Yes":

        for row in read_students():
            if row[1]==roll:
                exists=True
            else:
                updated.append(row)
        
        if exists:
            with open(filename, "w", newline="") as file:
                write = csv.writer(file)
                write.writerows(updated)
            print("Student record deleted successfully!")
        else:
            print("Student not found !")

    else:
        print("Operation Aborted")

@log_activity
def calculate_average():
    avg=0
    count=0
    for row in read_students():
        avg+= float(row[3])
        count+=1

    if count > 0:
        average = avg / count
        print(f"The average of {count} students out of 100 marks is {average}")
    else:
        print("NO RECORDS FOUND")

@log_activity
def students_above_75():
    found=False
    print(f"---THE DETAILS STUDENTS WHOSE MARKS ARE ABOVE 75---")
    print(f"{'Name':<30}{'Roll No':<15}{'Course':<30}{'Marks':<10}")
    for row in filtered_students_above_75():
        found=True
        print(f"{row[0]:<30}{row[1]:<15}{row[2]:<30}{row[3]:<10}")
    print("-" * 85)

    if not found:
        print("NO STUDENT WITH ABOVE 75 MARKS")
    

