# Function	Responsibility
# add_student()	Add a new student
# view_students()	Display all students
# search_student()	Find student by roll number
# update_student()	Update existing student details
# delete_student()	Delete a student
# calculate_average()	Calculate average marks
# students_above_75()   Display students scoring above 75

import csv

filename=r"C:\Users\Dell\Documents\CLG NOTESSSSSSS\EXTRA\week4-project\data\student.csv"

def add_student():
    num=int(input("Enter the number of students to add: "))

    for i in range(num):
        name=input("Enter Student name: ").capitalize()
        roll=input("Enter Student roll number: ")
        marks=float(input("Enter Sutudent marks(0-100): "))

        with open(filename,"r",newline="") as file:
            read=csv.reader(file)
            for row in read:
                if row[1]==roll:
                    print("Student with this roll number already exists!")
                    return

        with open(filename,"a",newline="") as file:
            write=csv.writer(file)

            write.writerow([name,roll,marks])

        print(f"Student {name} added")

    print("Data saved !")
    print("-"*30)

def view_students():
    print("\t---DISPLAYING STUDENT DETAILS---")
    with open(filename,"r",newline="") as file:
        read=csv.reader(file)
        print(f"{'Name':<30}{'Roll No':<15}{'Marks':<10}")
        for row in read:
            print(f"{row[0]:<30}{row[1]:<15}{row[2]:<10}")
        print("-" * 45)

def search_student():
    roll=input("Enter Student roll number to search: ")

    with open(filename,"r",newline="") as file:
        read=csv.reader(file)
        found=False
        for row in read:
            if row[1]==roll:
                found=True
                print("Student found")
                print("Student details:")
                print(f"Name: {row[0]}")
                print(f"Roll Number: {row[1]}")
                print(f"Marks: {row[2]}")

        if found==False:
            print(f"Student having roll number:{roll} not found !")

def update_student():
    roll=input("Enter the student roll number you want to update: ")
    exists=False
    update=[]
    with open(filename,"r",newline="") as file:
        read=csv.reader(file)

        for row in read:
            if row[1]==roll:
                exists=True
                print("update the details here:")
                name=input("Enter Student name: ").capitalize()
                marks=float(input("Enter Sutudent marks(0-100): "))
                row[0]=name
                row[2]=marks
            update.append(row)

    if exists:
        with open(filename,"w",newline="") as file:
            write=csv.writer(file)
            write.writerows(update)

            print("Details updated!")
    else:
        print("student not found!")

def delete_student():
    roll=input("Enter the roll number you want to delete: ")
    exists=False
    updated=[]
    with open(filename,"r",newline="") as file:
        read=csv.reader(file)

        for row in read:
            if row[1]==roll:
                exists=True
                print(f"student of roll no {roll} deleted!")
            else:
                updated.append(row)

    if exists:
        with open(filename, "w", newline="") as file:
            write = csv.writer(file)
            write.writerows(updated)
        print("Student record deleted successfully!")
    else:
        print("Student not found !")


# ---test purpose function
def read_csv():
    try:
        with open(filename,"r") as file:
            r=csv.reader(file)
            for i in r:
                print(i[2])
    except FileNotFoundError:
        print("file not found")

# read_csv()