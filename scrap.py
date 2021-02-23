#python3 scrap.py "product_name_1" "product_name_2" ...

import requests
import json
import sys
import mysql.connector

""" 
For SQL Connection
------------------
Parameters
----------
    -host
    -user
    -password
    -database name
    -password format
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mindfire@1",
  database="product_database",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

"""
GET PRODUCT
-----------
Parameters
-----------
    -name : takes the product name for scraping it from the respectively api.
Returns
-------
    It return an array of JSON data, containg all the product details..
"""

def get_products(name):
        headers = {
            "apikey": "b21cb260-6cee-11eb-ac9b-91d366011407"
        }

        params = (
            ("url", "https://www.walmart.com/grocery/v4/api/products/search?count=60&offset=0&page=1&storeId=2086&query=" + name),
        )

        try:
            response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
            response_data = response.json()
            if 'products' in response_data:
                return response_data['products']
        except Exception as e:
            print('Error in scraping data from Zenscrape: {}'.format(str(e)))
            return []

# Query for Inserting the data into the database
sql = "INSERT INTO Products (name, price) VALUES (%s, %s)"

# It will take the product names from command line argument.
n = len(sys.argv)
for i in range(1,n):
    products = get_products(sys.argv[i])
    products_json = json.dumps(products)
    products_data = json.loads(products_json)
    val = []
    for i in range(len(products_data)):
        val.append((products_data[i]['basic']['name'],products_data[i]['store']['price']['displayPrice']))
        # print(products_data[i]['store']['price']['displayPrice'])
    mycursor.executemany(sql, val)

mydb.commit()

    


