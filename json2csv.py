
import json,csv

fp1 = open("emp.json",'r')

fp2 = open("emp.csv",'w',newline='')

users = json.load(fp1)

print((users))

new_users = []

for user in users:
    new_users.append((user['uid'],user['uname'],user['gender']))


    print(new_users)

cw = csv.writer(fp2)
cw.writerow(['uid','uname','gender'])
cw.writerows(new_users)
print("data written to csv file")
fp1.close()
fp2.close()


