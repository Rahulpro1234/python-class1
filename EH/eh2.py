
try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))

    print(a/b)

except ZeroDivisionError as e:
    print(e)
except ValueError as ve:
    print(ve)
    print("Invalid input") 