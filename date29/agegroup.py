age = int(input("Enter Your Age"))
if(age > 7 and age < 12):
    print("Childhood")
elif(age > 13 and age < 17):
    print("teenage")
elif(age > 18 and age < 40):
    print("Adult")
elif(age > 41 and age < 60):
    print("old age")
elif(age < 61):
    print("Senior ctizen")
else:
    print("enter valid age")
