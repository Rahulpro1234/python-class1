





details = [{"id":1,"first_name":"Peyter","last_name":"Oppery","email":"poppery0@ebay.com","gender":"Male","ip_address":"193.170.144.228"},
{"id":2,"first_name":"Brendon","last_name":"Jervois","email":"bjervois1@google.com.br","gender":"Male","ip_address":"48.83.241.156"},
{"id":3,"first_name":"Noah","last_name":"Adrian","email":"nadrian2@xrea.com","gender":"Male","ip_address":"48.108.131.108"},
{"id":4,"first_name":"Isacco","last_name":"Lambersen","email":"ilambersen3@umich.edu","gender":"Male","ip_address":"72.131.49.244"},
{"id":5,"first_name":"Humfried","last_name":"Soulsby","email":"hsoulsby4@mozilla.org","gender":"Male","ip_address":"75.152.70.219"},
{"id":6,"first_name":"Brunhilda","last_name":"Tiddeman","email":"btiddeman5@salon.com","gender":"Female","ip_address":"44.142.124.25"},
{"id":7,"first_name":"Eddie","last_name":"Eayrs","email":"eeayrs6@ibm.com","gender":"Male","ip_address":"173.165.202.123"},
{"id":8,"first_name":"Fara","last_name":"Noore","email":"fnoore7@bravesites.com","gender":"Female","ip_address":"18.241.164.35"},
{"id":9,"first_name":"Vilma","last_name":"Fiddyment","email":"vfiddyment8@hud.gov","gender":"Female","ip_address":"176.131.76.207"},
{"id":10,"first_name":"Neel","last_name":"Chesswas","email":"nchesswas9@vkontakte.ru","gender":"Male","ip_address":"126.242.204.186"}]

no_of_products = 0
for detail in details:
    if detail['gender'] == 'Female':
        no_of_products = no_of_products + 1
print(no_of_products)
# print(len('details'))
# print(len(details))



