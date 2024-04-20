"""
Program: db.py
Author: Khilfi
Perform database operations for reading, and saving data from all text file.
"""
import datetime as dt


def loadOrders():
  orders: list[dict] = []
  with open('orders.txt') as file:
    next(file)  # Skip data header
    for line in file:
      (id, userId, address, datetime, status, totalPrice, *products_) = line.split(',')  

      # Parse products into list of dictionaries
      i = 2
      products = []
      while i < len(products_):
        products.append({
          "id": products_[i-2],
          "price": float(products_[i-1]),
          "quantity": int(products_[i])
        })
        i += 3

      orders.append({
        "id": id,
        "userId": userId,
        "address": address,
        "datetime": datetime,
        "status": True if status == "True" else False,
        "totalPrice": float(totalPrice),
        "products": products
      })
  
  return orders


def saveOrders(orders: list[dict]):
  header = "id,userId,address,datetime,status,totalPrice,productId,price1,productId2,price2,...,productIdN,priceN"
  raw_data = header + '\n'
  for order in orders:
    raw_data += f'{order["id"]},{order["userId"]},{order["address"]},{order["datetime"]},{order["status"]},{order["totalPrice"]}'

    for product in order["products"]:
      v = list(product.values())
      while len(v) > 0:
        raw_data += f',{v.pop(0)},{v.pop(0)},{v.pop(0)}'
    raw_data += '\n'

  with open('orders.txt', 'w') as file:
    file.write(raw_data)



if __name__ == "__main__":
  print("TEST 1")
  orders = loadOrders()
  print(orders)
  print("TEST 2")
  orders.append({
    "id": "3",
    "userId": "10",
    "address": "INTEC Education College",
    "datetime": "2024",
    "status": False,
    "totalPrice": 10.00,
    "products": [{"id": "4", "price": 10.00, "quantity": 1}]

  })
  saveOrders(orders)
