rows = int(input("Enter the row number"))
for i in range(rows):
    for j in range(i+1):
        print("*", end=' ')
    print('')
