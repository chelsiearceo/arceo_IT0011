# Part a: Using nested for statement
def pattern_a():
    for i in range(1, 6):
        print(' ' * (5 - i) + ''.join(str(j) for j in range(1, i + 1)))

# Part b: Using nested while statement
def pattern_b():
    i = 1
    while i <= 7:
        if i % 2 != 0:
            print(' ' * (7 - i) + str(i) * i)
        i += 1

# Call the functions to display the patterns
pattern_a()
print()  # For separating the two patterns
pattern_b()
# Part a: Using nested for statement
def pattern_a():
    for i in range(1, 6):
        print(' ' * (6 - i) + ''.join(str(j) for j in range(1, i + 1)))

# Part b: Using nested while statement
def pattern_b():
    i = 1
    while i <= 7:
        if i % 2 != 0:
            print(str(i) * i)
        i += 1

# Call the functions to display the patterns
pattern_a()
print()  # For separating the two patterns
pattern_b()