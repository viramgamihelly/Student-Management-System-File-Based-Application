import csv

def read_csv():
    try:
        with open(r"C:\Users\Dell\Documents\CLG NOTESSSSSSS\EXTRA\week4-project\data\student.csv","r") as file:
            r=csv.reader(file)
            for i in r:
                print(i)
    except FileNotFoundError:
        print("file not found")

read_csv()