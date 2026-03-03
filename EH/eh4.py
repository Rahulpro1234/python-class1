
#without err handling

# fp = None
# fp = open("test.txt", "r")
# data = fp.read()
# print(data)

# fp.close()  

#with err handling

try:
    fp = open("test.txt", "r")

except Exception as e:
    fp = open("default.txt", "r")
    data = fp.read()
    print(data)
    print(e)
    
finally:
    fp.close()


