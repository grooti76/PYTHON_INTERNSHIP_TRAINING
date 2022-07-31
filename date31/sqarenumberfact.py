n = int(input("Enter the Number"))


def function(n):
    if(n < 0):
        return 0
    elif(n == 0 or n == 1):
        return 1
    else:
        return n**1+function(n-1)


sum = function(n)
print("The square sum result of", n, "is", sum)
