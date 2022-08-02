num = int(input("Enter the Number you want to get the table: "))
myFile = open("table.txt", "w")

for x in range(1, 11):
    table = num*x
    table1 = (num, "x", x, "=", table)
    myFile.write(str(table1, "\n"))
myFile = open("table.txt", "r")
x = myFile.read()
print(x)
myFile.close()
