
# invoke Apis and print all usernames

import requests

# resp = requests.get('https://dummyjson.com/products')

# data = resp.json()

# for product in data["products"]:
#     if product["category"] == "beauty":
#      print (product["title"])



resp = requests.get('https://dummyjson.com/products')
data = resp.json()

products = data["products"]
i = 0
while i < len(products):
    if products[i]["category"] == "beauty":
        print(products[i]["title"])
    i += 1












