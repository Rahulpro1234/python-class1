
fp1=open('abc.txt','r')
fp2= open('data.txt','w')

print(fp1.readable()) #true
print(fp1.writable()) #false
print(fp1.name)  #abc.txt
print(fp1.mode)  #r
print(fp1.closed)  #false


