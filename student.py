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
        roll=int(input("Enter Student roll number: "))
        marks=float(input("Enter Sutudent marks(0-100): "))

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




    

#---test purpose function
# def read_csv():
#     try:
#         with open(filename,"r") as file:
#             r=csv.reader(file)
#             for i in r:
#                 print(i)
#     except FileNotFoundError:
#         print("file not found")

# read_csv()