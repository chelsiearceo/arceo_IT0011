fname = input ("Enter first name: ")
lname = input ("Enter last name: ")

print("====================================================")
print("Full Name:", fname, lname)
print("Full Name (Upper Case):", fname.upper(), lname.upper())
print("Full Name (Lower Case):", fname.lower(), lname.lower())

FullName = fname + " " + lname
print("Length of Full Name:", len(FullName))