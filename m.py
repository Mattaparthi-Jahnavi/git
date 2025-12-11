def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a - b
    return a * b 

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b



def main():
    print("\n--- Simple Calculator + Fibonacci ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Fibonacci")
    print("6. Exit & END")

    while True:
        choice = input("\nEnter your choice (1-6): ")

        if choice in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
                
        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select between 1-6.")


if __name__ == "__main__":
    main()
