import requests
import json
import sys
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mindfire@1",
  database="product_database",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

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
sql = "INSERT INTO Products (name, price) VALUES (%s, %s)"
n = len(sys.argv)
for i in range(1,n):
    products = get_products(sys.argv[i])
    print(products)
    products_json = json.dumps(products)
    products_data = json.loads(products_json)
    val = []
    for i in range(len(products_data)):
        val.append((products_data[i]['basic']['name'],products_data[i]['store']['price']['displayPrice']))
    mycursor.executemany(sql, val)

mydb.commit()

    


