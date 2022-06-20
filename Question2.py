#Question 2 of the worksheet
emp = []
age = []

num = int(input("Enter the number of employees: "))
for i in range(0, num):
    a = input("Enter the name of the employee: ")
    emp.append(a)
print()
for j in range(0, num):
    b = input("Enter the age of the employee: ")
    age.append(b)
for x in range(0, num):
    print("Name: ", emp[x], "Age: ", age[x])
