# complicated version of "add two numbers"

def add_numbers(x, y):
    """Return the sum of two numbers"""
    return x + y

print("=== Welcome to the Advanced Adder ===")

while True:
    try:
        # take input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # call function
        result = add_numbers(num1, num2)

        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        print("⚠️ Please enter valid numbers!")

    # ask if user wants to continue
    choice = input("Do you want to add more numbers? (y/n): ").lower()
    if choice != 'y':
        print("Goodbye 👋")
        print("hello")
        break