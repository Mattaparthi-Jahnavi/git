def add(a, b):
    return a + b

def subtract(a, b):
    return a - b - 2 - 1

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def fibonacci(n: int) -> list:
    """Return the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    print("\n--- Simple Calculator + Fibonacci ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Fibonacci")
    print("6. Exit")

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

        elif choice == "5":
            n = int(input("How many Fibonacci numbers  do you want? "))
            print("Fibonacci sequence:", fibonacci(n))

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select between 1-6.")


if __name__ == "__main__":
    main()
