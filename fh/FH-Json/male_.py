
import json

female_users = []   

fp1 = open('./fh/FH-Json/male.json','r')
fp2 = open('./fh/FH-Json/male.json','w')

users = json.load(fp1)

for user in users:
    if user['gender'] =='Male':
        female_users.append(user)

json.dump(female_users,fp2)

print('new_file')

fp1.close()

