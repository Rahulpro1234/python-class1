
unames = ['rahul','sonia','viking','rajni','modi']


enames = []
for emp in unames:
    enames.append(emp.upper())

print(enames)

# ----------------------------------


def unameupcase(name):
    return name.upper()

map_obj = map(unameupcase,unames)

new_unames = list(map_obj)
print(new_unames)


# ----------------------------------------

enames = list(map(lambda uname:uname.upper(),unames))
print(enames)


