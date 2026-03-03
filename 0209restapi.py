
import requests

# resp = requests.get('https://dummyjson.com/products')
# product_data = resp.json()
# products = product_data['products']
# print(type(products))
# print(len(products))

# # reduced lines of same code
# import requests
# for product in requests.get('https://dummyjson.com/products').json()['products']:
#     print(product['title'])


# # print number of beauty products

# # no_of_beauty_products = 0
# # for product in requests.get('https://dummyjson.com/products').json()['products']:


# actors = [
#     {
#         "id": 1,
#         "name": "Jack Nicholson"
#     },
#     {
#         "id": 2,
#         "name": "Charlize Theron"
#     },
#     {
#         "id": 3,
#         "name": "Heath Ledger"
#     },
#     {
#         "id": 4,
#         "name": "Julia Roberts"
#     },
#     {
#         "id": 5,
#         "name": "Al Pacino"
#     },
#     {
#         "id": 6,
#         "name": "Jake Gyllenhaal"
#     },
#     {
#         "id": 7,
#         "name": "Leonardo DiCaprio"
#     },
#     {
#         "id": 8,
#         "name": "Anne Hathaway"
#     },
#     {
#         "id": 9,
#         "name": "Morgan Freeman"
#     },
#     {
#         "id": 10,
#         "name": "Leonardo DiCaprio"
#     },
#     {
#         "id": 11,
#         "name": "Mark Ruffalo"
#     },
#     {
#         "id": 12,
#         "name": "Jack Nicholson"
#     },
#     {
#         "id": 13,
#         "name": "Jack Nicholson"
#     },
#     {
#         "id": 14,
#         "name": "Brad Pitt"
#     },
#     {
#         "id": 15,
#         "name": "Denzel Washington"
#     },
#     {
#         "id": 16,
#         "name": "Heath Ledger"
#     },
#     {
#         "id": 17,
#         "name": "Gal Gadot"
#     },
#     {
#         "id": 18,
#         "name": "George Clooney"
#     },
#     {
#         "id": 19,
#         "name": "Heath Ledger"
#     },
#     {
#         "id": 20,
#         "name": "Robert Downey Jr."
#     },
#     {
#         "id": 21,
#         "name": "Florence Pugh"
#     },
#     {
#         "id": 22,
#         "name": "Keanu Reeves"
#     },
#     {
#         "id": 23,
#         "name": "Christian Bale"
#     },
#     {
#         "id": 24,
#         "name": "Chris Hemsworth"
#     },
#     {
#         "id": 25,
#         "name": "Morgan Freeman"
#     },
#     {
#         "id": 26,
#         "name": "Daniel Radcliffe"
#     },
#     {
#         "id": 27,
#         "name": "Scarlett Johansson"
#     },
#     {
#         "id": 28,
#         "name": "Tom Hanks"
#     },
#     {
#         "id": 29,
#         "name": "Natalie Portman"
#     },
#     {
#         "id": 30,
#         "name": "Meryl Streep"
#     },
#     {
#         "id": 31,
#         "name": "Jack Nicholson"
#     },
#     {
#         "id": 32,
#         "name": "Ryan Gosling"
#     },
#     {
#         "id": 33,
#         "name": "Denzel Washington"
#     },
#     {
#         "id": 34,
#         "name": "Tom Cruise"
#     },
#     {
#         "id": 35,
#         "name": "Emma Stone"
#     },
#     {
#         "id": 36,
#         "name": "Emma Stone"
#     },
#     {
#         "id": 37,
#         "name": "Scarlett Johansson"
#     },
#     {
#         "id": 38,
#         "name": "Ryan Gosling"
#     },
#     {
#         "id": 39,
#         "name": "Jack Nicholson"
#     },
#     {
#         "id": 40,
#         "name": "Jake Gyllenhaal"
#     },
#     {
#         "id": 41,
#         "name": "George Clooney"
#     },
#     {
#         "id": 42,
#         "name": "Benedict Cumberbatch"
#     },
#     {
#         "id": 43,
#         "name": "Adam Driver"
#     },
#     {
#         "id": 44,
#         "name": "Will Smith"
#     },
#     {
#         "id": 45,
#         "name": "Zendaya"
#     },
#     {
#         "id": 46,
#         "name": "Denzel Washington"
#     },
#     {
#         "id": 47,
#         "name": "Timoth\u00e9e Chalamet"
#     },
#     {
#         "id": 48,
#         "name": "Gal Gadot"
#     },
#     {
#         "id": 49,
#         "name": "Florence Pugh"
#     },
#     {
#         "id": 50,
#         "name": "Samuel L. Jackson"
#     },
#     {
#         "id": 51,
#         "name": "Scarlett Johansson"
#     },
#     {
#         "id": 52,
#         "name": "George Clooney"
#     },
#     {
#         "id": 53,
#         "name": "Jennifer Lawrence"
#     },
#     {
#         "id": 54,
#         "name": "Heath Ledger"
#     },
#     {
#         "id": 55,
#         "name": "Charlize Theron"
#     },
#     {
#         "id": 56,
#         "name": "Timoth\u00e9e Chalamet"
#     },
#     {
#         "id": 57,
#         "name": "Anne Hathaway"
#     },
#     {
#         "id": 58,
#         "name": "Tom Cruise"
#     },
#     {
#         "id": 59,
#         "name": "Anne Hathaway"
#     },
#     {
#         "id": 60,
#         "name": "Morgan Freeman"
#     },
#     {
#         "id": 61,
#         "name": "Meryl Streep"
#     },
#     {
#         "id": 62,
#         "name": "Ryan Gosling"
#     },
#     {
#         "id": 63,
#         "name": "Ryan Gosling"
#     },
#     {
#         "id": 64,
#         "name": "Jake Gyllenhaal"
#     },
#     {
#         "id": 65,
#         "name": "Jack Nicholson"
#     },
#     {
#         "id": 66,
#         "name": "Hugh Jackman"
#     },
#     {
#         "id": 67,
#         "name": "Benedict Cumberbatch"
#     },
#     {
#         "id": 68,
#         "name": "Chris Evans"
#     },
#     {
#         "id": 69,
#         "name": "Samuel L. Jackson"
#     },
#     {
#         "id": 70,
#         "name": "Mark Ruffalo"
#     },
#     {
#         "id": 71,
#         "name": "Tom Cruise"
#     },
#     {
#         "id": 72,
#         "name": "Tom Hanks"
#     },
#     {
#         "id": 73,
#         "name": "Chris Hemsworth"
#     },
#     {
#         "id": 74,
#         "name": "Daniel Radcliffe"
#     },
#     {
#         "id": 75,
#         "name": "Leonardo DiCaprio"
#     },
#     {
#         "id": 76,
#         "name": "George Clooney"
#     },
#     {
#         "id": 77,
#         "name": "George Clooney"
#     },
#     {
#         "id": 78,
#         "name": "Florence Pugh"
#     },
#     {
#         "id": 79,
#         "name": "Hugh Jackman"
#     },
#     {
#         "id": 80,
#         "name": "Morgan Freeman"
#     },
#     {
#         "id": 81,
#         "name": "George Clooney"
#     },
#     {
#         "id": 82,
#         "name": "Al Pacino"
#     },
#     {
#         "id": 83,
#         "name": "Leonardo DiCaprio"
#     },
#     {
#         "id": 84,
#         "name": "Benedict Cumberbatch"
#     },
#     {
#         "id": 85,
#         "name": "Denzel Washington"
#     },
#     {
#         "id": 86,
#         "name": "Robert Downey Jr."
#     },
#     {
#         "id": 87,
#         "name": "Anne Hathaway"
#     },
#     {
#         "id": 88,
#         "name": "Mark Ruffalo"
#     },
#     {
#         "id": 89,
#         "name": "Benedict Cumberbatch"
#     },
#     {
#         "id": 90,
#         "name": "Anne Hathaway"
#     },
#     {
#         "id": 91,
#         "name": "Daniel Radcliffe"
#     },
#     {
#         "id": 92,
#         "name": "Chris Hemsworth"
#     },
#     {
#         "id": 93,
#         "name": "Morgan Freeman"
#     },
#     {
#         "id": 94,
#         "name": "Florence Pugh"
#     },
#     {
#         "id": 95,
#         "name": "Johnny Depp"
#     },
#     {
#         "id": 96,
#         "name": "Natalie Portman"
#     },
#     {
#         "id": 97,
#         "name": "Leonardo DiCaprio"
#     },
#     {
#         "id": 98,
#         "name": "Gal Gadot"
#     },
#     {
#         "id": 99,
#         "name": "Tom Hanks"
#     },
#     {
#         "id": 100,
#         "name": "Gal Gadot"
#     }
# ]

# for actor in actors:
#     print(actor['id'])


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




# no_of_products = 0
# for detail in details:
#     if detail['id'] == 1:
#         no_of_products = no_of_products + 1
# print(no_of_products)
# print(len('details'))



