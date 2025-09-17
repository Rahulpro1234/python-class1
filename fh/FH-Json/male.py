
import json

male_users = []
female_users=[]

fp1 = open('./fh/FH-Json/users.json','r')
fp2 = open('./fh/FH-Json/male.json','w')
fp3 = open('./fh/FH-Json/female.json','w')


users = json.load(fp1)

for user in users:
    if user['gender'] =='Male':
        male_users.append(user)

    elif user['gender'] =='Female':
        female_users.append(user)

json.dump(male_users,fp2)
json.dump(female_users,fp3)

print('new_file')

fp1.close()
fp2.close()
fp3.close()
 