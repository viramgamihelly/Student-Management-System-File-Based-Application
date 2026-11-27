from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    calculate_average,
    students_above_75
)

def main_menu():

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average Marks")
        print("7. Students Above 75 Marks")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            calculate_average()

        elif choice == "7":
            students_above_75()

        elif choice == "8":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main_menu()