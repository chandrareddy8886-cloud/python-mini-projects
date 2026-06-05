# apperence of menu
def menu():
    calculator = """ --------------\n | Terminal   |\n | calculator | \n --------------"""
    print(calculator)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    first = int(input(">>>>Enter the first number ="))
    operator = (input(">>>>Select the operator ="))
    second = int(input(">>>Enter the second number ="))

    if operator == "1":
        print("Result =",first+second)
    elif operator == "2":
        print("Result =",first-second)
    elif operator == "3":
        print("Result =",first*second)
    elif operator == "4":
        if second == 0:
            print("not divisible by 0")
        else:
            print("Result =",first/second)
    else:
        print("enter listed operator")


again = input("press 0 for menu =")
if again == "0":
    menu()