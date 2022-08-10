try:
    a = int(input("Enter the First number: "))
    b = int(input("Enter the Second number: "))
    c = a/b
    print("The division of", a, "and", b, "is", c)
except Exception as e:
    print("Exception Occur, Division only done with Integer")
print("Thanks for using our software")
