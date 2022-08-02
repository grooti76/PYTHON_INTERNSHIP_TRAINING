n = int(input("Enter the Number"))


def function(n):
    if(n <= 0):
        return 0
    else:
        return 1/n+function(n-1)


sum = function(n)
print("The factorial of", n, "is", sum)
