fname = input ("Enter first name: ")
lname = input ("Enter last name: ")
age = int(input("Enter age: "))

full_name = fname + " " + lname
sliced_name = fname[0:4]
greeting = "Hello, {}! Welcome. You are {} years old.".format(sliced_name, age)

print("========================================================================")
print("Full Name:", full_name)
print("Sliced Name:", sliced_name)
print("Greeting Message:", greeting)