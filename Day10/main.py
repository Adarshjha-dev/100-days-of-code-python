import art


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(art.logo)
    continue_previous = True
    num1 = float(input("Enter the first number: "))

    while continue_previous:
        print("+\n-\n*\n/")
        operator = input("Select an operation: ")
        num2 = float(input("Enter the second number: "))
        result = operations[operator](num1, num2)
        print(f"{num1}{operator}{num2} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start over. "
        ).lower()
        if choice == "y":
            num1 = result
        elif choice == "n":
            continue_previous = False
            print("\n" * 10)
            calculator()


calculator()
