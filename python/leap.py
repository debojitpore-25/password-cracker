year=int(input("Enter the year to check if the year is a leap year or not : "))

if(year%400==0):
    print("This is a leap year ")
elif(year%4==0):
    print("This is a leap year  ")
elif(year%100==0):
    print("This year is not a leap year")
else:
    print("This year is not a Leap year.")