marks = int(input("Enter the Marks: "))
if(marks > 90 and marks <= 100):
    print("Grade: A")
elif(marks > 80 and marks <= 90):
    print("Grade: B")
elif(marks > 70 and marks <= 79):
    print("Grade: C")
elif(marks > 60 and marks <= 69):
    print("Grade: D")
elif(marks > 50 and marks <= 59):
    print("Grade: E")
elif(marks > 40 and marks <= 49):
    print("Grade: F")
else:
    print("Fail")
