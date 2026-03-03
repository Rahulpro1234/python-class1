
# numbers = [1, 2, 3, 4, 5, 6]
# --------------------------------------- list comprehension
# new_list = [x + 1 for x in numbers]
# print(new_list)
# ------------------------------------- -- explicit for loop
# new_numbers = []
# for num in numbers:
#     new_numbers.append(num + 1)
# print(new_numbers)
# --------------------------------------- lambda function with map
# print(list(map(lambda x: x + 1, numbers)))

# ---------------------------------------  named function with map
# def add_one(x):
#     return x + 1
# print(list(map(add_one, numbers)))

# ---------------------------------------

# staticmethod and classmethod in Python
# class test:
#     def method1(self):
#         print("m1 method.")

#     @classmethod
#     def method2(cls):
#         print("m2 class method.")

#     @staticmethod
#     def method3():
#         print("m3 static method.")  
# t1 = test()
# t2 = test()
# t1.method1()
# t2.method2()
# t1.method3()

# ---------------------------------------

# class Account:

#     def open_account(self):
#        print("Account opened")

#     def deposit_amount(self,amount):
#         print("amount Deposited successfully"," Thank you" )


# a1 = Account()
# a1.open_account()
# a1.deposit_amount(10000)
# a1.deposit_amount(20000)
# a1.deposit_amount(30000)




    







