def divide(a, b):
    if b == 0:
        return None
    return a/b

def exponentiation(a, b):
    return a**b
    
def remainder(a, b):
    if b == 0:
        return None
    return a%b
    
def summation(a, b):
    if a > b:
        return None
    return sum(range(a, b + 1))
    
def main():
    while True:
        print("Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")
        
        choice = input("Enter your choice: ").upper()
        if choice == "X":
            print("Thank you! Exiting the program now...")
            break
        
        try:
            a = int(input("Enter the first digit: "))
            b = int(input("Enter the second digit: "))
            
            if choice == "D":
                result = divide(a, b)
            elif choice == "E":
                result = exponentiation(a, b)
            elif choice == "R":
                result = remainder(a, b)
            elif choice == "F":
                result = summation(a, b)
            else:
                print("Invalid input. Pleasy try again.")
                continue
            
            if result is None:
                print("Invalid input for the chosen operation.")
            else:
                print(f"Result: {result}")
        except ValueError:
                print("Invalid input. Please enter a digit.")
    
if __name__ == "__main__":
    main()