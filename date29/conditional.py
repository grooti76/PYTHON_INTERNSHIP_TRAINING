time = int(input("Enter the Time: "))
if(time > 3 and time < 12):
    print("good morning")
elif(time > 12 and time < 16):
    print("Good Afternoon")
elif(time > 16 and time < 24 or time < 3):
    print("Good Night")
else:
    print("Enter the correct time in 24h format")
