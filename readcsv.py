import csv 

fp = open("emp.csv",'r')

emp_data = csv.reader(fp)
employees = list(emp_data)
print(type(emp_data))

for emp in employees:
    print(emp)

