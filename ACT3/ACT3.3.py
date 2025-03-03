lname = input("Enter last name: ")
fname = input("Enter first name: ")
age = input("Enter age: ")
contact = input("Enter contact number: ")
course = input("Enter course: ")

stud_info = f"Last Name: {lname}\nFirst Name: {fname}\nAge: {age}\nContact Number: {contact}\nCourse: {course}\n\n"
f = open('students.txt', 'a')
f.writelines(stud_info)
f.close()

print("Student information has been saved to 'students.txt'.")