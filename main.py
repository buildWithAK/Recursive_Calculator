import art


# TODO : Write out the 4 functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero."
    return n1 / n2

# TODO : Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO : Take user input values for operands and operation
# TODO : Display the result obtained
# TODO : Program asks if the user wants to continue working with the previous result.
    # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    # If no, program asks the user for the fist number again and wipes all memory of previous calculations.

# TODO : IMPORTANT FUNCTIONALITY :
#  We used recursion in this program to repetitively call the function at the end of execution

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print (symbol)
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation.")
            continue

        num2 = float(input("What is the next number?: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        # TODO: The program asks the user for a choice; keeps on running until user enters valid choice
        while True:
            choice = input(
                f"Type 'y' to continue calculating with {result}, "
                "type 'n' to start a new calculation, "
                "or type 'end' to exit: "
            ).lower()

            if choice == "y":
                num1 = result
                break

            elif choice == "n":
                print("\n" * 20)
                return calculator()

            elif choice == "end":
                print("Calculator closed.")
                return None

            else:
                print("Invalid choice. Please enter 'y', 'n', or 'end'.")
    return None


# TODO: Calling function calculator
calculator()
