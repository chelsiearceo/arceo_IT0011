import os

students = []

def calculate_grade(class_standing, major_exam):
    return (class_standing * 0.6) + (major_exam * 0.4)

def show_all_students():
    if not students:
        print("No student records found.")
        return
    print("\nAll Student Records:")
    for s in students:
        final_grade = calculate_grade(s[2], s[3])
        print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}, Final Grade: {final_grade:.2f}")

def sort_by_last_name():
    students.sort(key=lambda s: s[1][1])
    print("Sorted by last name.")

def sort_by_grade():
    students.sort(key=lambda s: calculate_grade(s[2], s[3]), reverse=True)
    print("Sorted by grade.")

def show_student():
    student_id = input("Enter Student ID: ")
    for s in students:
        if s[0] == student_id:
            print(f"ID: {s[0]}, Name: {s[1][0]} {s[1][1]}, Class Standing: {s[2]}, Major Exam: {s[3]}")
            return
    print("Student not found.")

def add_student():
    sid = input("Enter 6-digit Student ID: ")
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append((sid, (fname, lname), class_standing, major_exam))
    print("Record added!")

def edit_student():
    student_id = input("Enter Student ID to edit: ")
    for i, s in enumerate(students):
        if s[0] == student_id:
            fname = input("Enter New First Name: ")
            lname = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing: "))
            major_exam = float(input("Enter New Major Exam: "))
            students[i] = (student_id, (fname, lname), class_standing, major_exam)
            print("Record updated!")
            return
    print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    global students
    students = [s for s in students if s[0] != student_id]
    print("Record deleted!")

def open_file():
    filename = input("Enter filename: ")
    filepath = f"ACT4/{filename}.txt" if not filename.endswith(".txt") else f"ACT4/{filename}"
    if not os.path.exists(filepath):
        print("File not found.")
        return
    with open(filepath, "r") as file:
        for line in file:
            row = line.strip().split(',')
            students.append((row[0], (row[1], row[2]), float(row[3]), float(row[4])))
    print(f"File {filepath} loaded!")

def save_file():
    filename = input("Enter filename: ")
    with open(filename, "w") as file:
        for s in students:
            file.write(f"{s[0]},{s[1][0]},{s[1][1]},{s[2]},{s[3]}\n")
    print("File saved!")

def save_as_file():
    if not os.path.exists("ACT4"):
        os.makedirs("ACT4")
    with open("ACT4/ACT4.txt", "w") as file:
        for s in students:
            file.write(f"{s[0]},{s[1][0]},{s[1][1]},{s[2]},{s[3]}\n")
    print("File saved!")

def main_menu():
    while True:
        print("\nStudent Record Management")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students")
        print("5. Sort by Last Name")
        print("6. Sort by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            save_as_file()
        elif choice == "4":
            show_all_students()
        elif choice == "5":
            sort_by_last_name()
        elif choice == "6":
            sort_by_grade()
        elif choice == "7":
            show_student()
        elif choice == "8":
            add_student()
        elif choice == "9":
            edit_student()
        elif choice == "10":
            delete_student()
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()