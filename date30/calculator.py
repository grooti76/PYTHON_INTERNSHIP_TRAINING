def add():
    a = int(input("Enter the First value"))
    b = int(("Enter the Second value"))
    c = a+b
    print("The sum of", a, "and", b, "is", c)


def sub():
    a = int(input("Enter the First value"))
    b = int(("Enter the Second value"))
    c = a-b
    print("The Difference of", a, "from", b, "is", c)


def mul():
    a = int(input("Enter the First value"))
    b = int(("Enter the Second value"))
    c = a*b
    print("The Multiplication of", a, "and", b, "is", c)


def div():
    a = int(input("Enter the First value"))
    b = int(("Enter the Second value"))
    c = a/b
    print("The division of", a, "to", b, "is", c)


inp = int(input('''Select the number from the given options
1. Addition
2. Subtraction
3. Multiplication
4. Division
'''))
if(inp == 1):
    add()
elif(inp == 2):
    sub()
elif(inp == 3):
    mul()
elif(inp == 3):
    div()
else:
    print("Please Select the Correct option")
