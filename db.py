"""
Program: db.py
Author: Khilfi, Murfiqah, Zainatul
Perform database operations for reading, and saving data from all text file.
"""


def loadOrders():
  orders: list[dict] = []
  with open('db/orders.txt') as file:
    next(file)  # Skip data header
    for line in file:
      (id, userId, address, datetime, status, productId, quantity, price) = line.split(',')  
      
      orders.append({
        "id": id,
        "userId": userId,
        "address": address,
        "datetime": datetime,
        "status": True if status == "True" else False,
        "productId": productId,
        "quantity": int(quantity),
        "price": float(price)
      })
  
  return orders


def saveOrders(orders: list[dict]):
  header = "id,userId,address,datetime,status,productId,quantity,price"
  raw_data = header + '\n'
  for order in orders:
    raw_data += f'{order["id"]},{order["userId"]},{order["address"]},{order["datetime"]},{order["status"]},{order["productId"]},{order["quantity"]},{order["price"]}\n'

  with open('db/orders.txt', 'w') as file:
    file.write(raw_data)


def saveProducts(stocks):
  file = open("db/products.txt", 'w')
  file.write("id,imageId,name,price,unit,sold,totalStars\n")
  for stock in stocks:
    file.write("{},{},{},{},{},{},{}\n".format(stock["id"], stock["imageId"], stock["name"], stock["price"], stock["unit"], stock["sold"], stock["totalStars"]))
  file.close()


def loadProducts():
  file = open('db/products.txt', 'r')
  next(file)  # Skip data header
  stocks = []
  for line in file:
    id_, imageId, name, price, unit, sold, totalStars = line.strip().split(",")
    stocks.append({
        "id": id_,
        "imageId": imageId,
        "name": name,
        "price": float(price),
        "unit": int(unit),
        "sold": int(sold),
        "totalStars": int(totalStars)
    })
  file.close()
  return stocks


def loadUsers():
  users = []
  with open('db/users.txt', 'r') as file:
    next(file)
    for line in file:
      id_, username, password = line.split(',')
      users.append({
          "id": id_,
          "username": username,
          "password": password,
      })
  return users


def saveUsers(users):
  header = "id,username,password"
  raw_data = header + '\n'
  for user in users:
    raw_data += f"{user['id']},{user['username']},{user['password'].strip()}\n"
  
  with open('db/users.txt', 'w') as file:
    file.write(raw_data)


if __name__ == "__main__":
  print("\nTEST 1: Load orders")
  orders = loadOrders()
  print(orders)

  print("\nTEST 2: Save orders (Refer orders.txt for output)")
  saveOrders(orders)

  print("\nTEST 3: Load products")
  overallProducts = loadProducts()
  for product in overallProducts:
      print(product)

  print("\nTEST 4: Save products (Refer products.txt for output)")
  saveProducts(overallProducts)

  print("\nTEST 5: loadUsers")
  users = loadUsers()
  print(users)

  print("\nTEST 6: saveUsers (Refer users.txt for output)")
  saveUsers(users)
