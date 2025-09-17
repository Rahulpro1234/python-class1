
def um():
    def login():
        print("login success")
    

    def logout():
        print("logout success")

        return logout()
    

fp = open('data.txt','r')
data = fp.read()
print(data)
