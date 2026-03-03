
# print(10/0) # ZeroDivisionError: division by zero

# Handling the exception

print(10/5)

try:
    print(10/0)
except ZeroDivisionError:
    print("You can't divide a number by zero") 




    