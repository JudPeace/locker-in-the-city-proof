import pandas as pd
import requests
import json

URL_API="http://localhost:5000/api"

def post_product(row):
    data = {'brand':row[0], 'type':row[1], 'calories':row[2], 'fats':row[3], 'sugar':row[4]}
    response = requests.post(URL_API+"/products", data = data).text
    return json.loads(response)['id']

def post_establishment(row):
    data = {'name':row[0], 'address':row[1], 'opening_time':row[2], 'closing_time':row[3]}
    requests.post(URL_API+"/establishments", data = data)

def post_prices(row):
    data = {'price':row[2]}
    name = row[0] 
    id = str(row[1])
    requests.post(URL_API+"/establishments/"+name+"/products/"+id+"/prices", data = data)

products = pd.read_csv("data/products.csv")
products['id'] = products.apply(post_product, axis=1)

establishments = pd.read_csv("data/establishments.csv")
establishments.apply(post_establishment, axis=1)

prices = pd.read_csv("data/prices.csv")
prices_products = prices.merge(products, on=['brand','type'], how='left')[['name', 'id', 'price']]
prices_products.apply(post_prices, axis=1)
