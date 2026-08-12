a=int(input("Enter the marks of the first subject : "))
b=int(input("Enter the marks of the second subject : "))
c=int(input("Enter the marks of the third subject : "))
d=int(input("Enter the marks of the fourth subject : "))
e=int(input("Enter the marks of the fifth subject : "))
f=int(input("Enter the marks of the sixth subject : "))
g=int(input("Enter the marks of the seventh subject : "))
h=int(input("Enter the marks of the eighth subject : "))
i=int(input("Enter the marks of the nineth subject : "))
j=int(input("Enter the marks of the tenth subject : "))

sum=a+b+c+d+e+f+g+h+i+j

print("The total of the total subjects : ",sum)

percentage=(sum)/10
print("The percentage is : ",percentage)

if percentage>=95:
    print("O Grade")
elif percentage>=85:
    print("A+ Grade")
elif percentage>=80:
    print("A Grade")
elif percentage>=75:
    print("B+ Grade")
elif percentage>=70:
    print("B Grade")
elif percentage>=60:
    print("C Grade")
elif percentage>=50:
    print("D Grade")
elif percentage>=35:
    print("Re-appear")
else:
    print("You Failed")
