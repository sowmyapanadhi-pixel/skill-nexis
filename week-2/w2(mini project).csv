#Student Management System
import csv
import os


FILE_NAME = "students.csv"


def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = input("Enter marks: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Roll Number", "Marks"])

        writer.writerow([name, roll_number, marks])

    print("Student added successfully!")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def search_student():
    roll_number = input("Enter roll number to search: ")

    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll_number:
                print("Student found!")
                print("Name:", student["Name"])
                print("Roll Number:", student["Roll Number"])
                print("Marks:", student["Marks"])
                found = True
                break

    if not found:
        print("Student not found.")


def delete_student():
    roll_number = input("Enter roll number to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] != roll_number:
                students.append(student)

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Name", "Roll Number", "Marks"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

    print("Student deleted successfully!")


while True:

    print("\n----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")