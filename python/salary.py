salary=int(input("Enter the basic salary : "))

hra=20/100*salary
da=15/100*salary
pf=10/100*salary

gsalary=salary+hra+da
nsalary=gsalary-pf

print("Gross Salary : ",gsalary)
print("Net Salary : ",nsalary)