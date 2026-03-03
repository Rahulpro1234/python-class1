
employees = [{"eid":101,"ename":"RG","gender":"male"},{"eid":102,"ename":"monica","gender":"female"},{"eid":103,"ename":"swathi","gender":"female"}]

employees = [{},{},{},{}]




for emp in employees:
    print('ename',emp['ename'])


# for employee in employees:
#     if employee['gender'] == 'male':
#         print('Emp name',employees['ename'])

for emp in employees:
    print(emp['ename'])

# we can iterate using for loop
# list,tuple,set,"rahul",string,range(10),bytes,bytearray,frozenset
no_of_male_employees=0
no_of_female_employees=0

# for emp in employees:
#     print(emp=emp + 1)
    
    


# byte data----

byte_data = bytes([10,20,30,242,232,235])
print(type(byte_data))

for data in byte_data:
    print(data)

# create dictionary

d1 = { }

emp = {
    'eid' :101,
    'ename':'rahul',
    'esal':45000,
    'email':'rg@gmail.com',
    'email':'rg@ibm.com'
}
# duplicate keys are not allowed

# read operation
print(d1)
print(type(d1))
print(emp)

# how to read dict values---

print(emp['eid'])
print(emp['ename'])
# print(emp['loc'])
# print(emp['avail'])

# update 

emp['ename']= 'rahulgandhi'

print(emp)

emp['avail'] = 'True'

# how to delete
# del emp['esal']

print(emp)


# what is random module-to generate random values--generate 10,4 digit otp numbers--
# for this you should import random and math library--so
import random,math
print(math.pi)
print(math.ceil(9.8))
print(random.randint(1000,9999))

from random import randint
for x in range(10):
    print(randint(1000,9999))

# pip install boto3 for installing AWS,S3,EC2.....





    







        