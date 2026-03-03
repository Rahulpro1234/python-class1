
def login(name,password):
    print("login success")
    return True,'10','20',[1,2,3]

st = login("RG","ILoveIndia")
print(st)

# -------------------------------------
def outer():
    print("outer function")

    def inner():
        print("inner function")


outer();

# inner();

# how to invoke inner fn from outside 

# def user_module():
#     def login():
#         pass
#     def logout():
#         pass


def user_module():
    def login():
        print('login sucess')
    
    def logout():
        pass

    return logout

inner = user_module()
inner()

print(type(inner))










