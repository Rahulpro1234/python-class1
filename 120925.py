
emp = {

    'eid' : 101,
    'ename':'Rahul',
    'esal':45000
}

print(emp['eid'])
print(emp['ename'])
print(emp['esal'])
# print(emp['loc'])   KeyError


# print all employee values
# print all employee keys
# print all employee values


print(emp['eid'])
print(emp.values())
print(type(emp.values()))

# top 25 errors and how to resolve errors
for value in emp.values():
    print(value)


products = {
  "students": [
    {
      "id": 1,
      "name": "Rahul",
      "age": 21,
      "course": "Computer Science"
    },
    {
      "id": 2,
      "name": "Anita",
      "age": 22,
      "course": "Electronics"
    },
    {
      "id": 3,
      "name": "Kiran",
      "age": 20,
      "course": "Information Technology"
    }
  ]
}

for  key in products.keys():
    print(key,":",products.get(key))

    # using get method----------------

from math import war2
print(war2(2))




