import pandas as pd
import random

products_brands = ["Kellogg's", "Nestlé", "Coca-Cola", "PepsiCo", "Danone", "Unilever", "Nescafé", "Lays", "Knorr"]
products_types = [
    ["Cereales", "Galletas", "Barras energéticas"],
    ["Chocolate", "Café", "Leche condensada"],
    ["Refrescos", "Agua mineral", "Té"],
    ["Refrescos", "Snacks", "Cereales"],
    ["Yogurt", "Bebidas vegetales", "Postres"],
    ["Higiene personal", "Productos de limpieza", "Helados"],
    ["Café instantáneo", "Capsulas de café", "Café molido"],
    ["Papas fritas", "Snacks", "Dips y salsas"],
    ["Sopas", "Salsas", "Condimentos"]
]

establishments = ["Mercadona", "Carrefour", "Dia", "Eroski", "Alcampo", "Lidl", "Aldi", "Hipercor", "El Corte Inglés"]
addresses = ["Calle del Sol 15", "Avenida de la Playa 28", "Plaza Mayor 7", "Calle del Carmen 12", "Avenida del Parque 89", "Calle de la Luna 52", "Paseo de la Alameda 76", "Calle del Mar 31", "Calle de la Paz 18"]

opening_times = ["08:00", "8:30", "9:00", "10:00"]
closing_times = ["14:00", "15:00", "20:00", "21:30"]

#products
brand_types=[[products_brands[i[0]], x]  for i in enumerate(products_types) for x in i[1]]
df_products = pd.DataFrame(brand_types, columns=["brand", "type"])
df_products['calories'] = random.sample(range(100,2000), len(df_products))
df_products['fats'] = random.sample(range(0,10000), len(df_products))
df_products['fats'] = df_products['fats']/100
df_products['sugar'] = random.sample(range(0,10000), len(df_products))
df_products['sugar'] = df_products['sugar']/100

df_products.to_csv('data/products.csv', index=False)

#establishments
df_establishments = pd.DataFrame({
    'name':establishments, 
    'address':addresses, 
    'opening_time':random.choices(opening_times, k=len(establishments)), 
    'closing_time':random.choices(closing_times, k=len(establishments))})
df_establishments.to_csv('data/establishments.csv', index=False)

#prices
df_products['key'] = 0
df_establishments['key'] = 0

df_prices = df_products.merge(df_establishments, on='key', how='outer')
df_prices = df_prices.sample(60).reset_index()
df_prices = df_prices[["brand", "type", "name"]]
df_prices["price"] = random.sample(range(0,10000), len(df_prices))
df_prices["price"] = df_prices["price"]/100

df_prices.to_csv('data/prices.csv', index=False)


