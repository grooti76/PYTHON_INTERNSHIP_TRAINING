n = int(input("Enter the Number"))


def function(n):
    if(n < 0):
        return 0
    elif(n == 0 or n == 1):
        return 1
    else:
        return n*function(n-1)


fact = function(n)
print("The factorial of", n, "is", fact)
