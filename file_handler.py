import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
filename = BASE_DIR / "data" / "student.csv"


def read_students():
    try:
        with open(filename, "r", newline="") as file:
            read = csv.reader(file)

            for row in read:
                yield row

    except FileNotFoundError:
        return

def add_student_record(student):
    with open(filename, "a", newline="") as file:
        write = csv.writer(file)
        write.writerow(student)

def save_students(records):
    with open(filename, "w", newline="") as file:
        write = csv.writer(file)
        write.writerows(records)
        
def filtered_students_above_75():
    for row in read_students():
        if float(row[3]) > 75:
            yield row