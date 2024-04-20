from breezypythongui import EasyFrame
import tkinter as tk
from db import loadOrders


items = loadOrders()


class ManagerDashboard(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, "Main Dashboard")
    self.addButton("Manage Products", 0, 0, command=self.manageProducts)

  def manageProducts(self):
    ProductManagement()


class ProductManagement(EasyFrame, tk.Toplevel):
  
  def __init__(self):
    EasyFrame.__init__(self, "Product Manager")
    tk.Toplevel.__init__(self)

    items = [
      {
        "id": "1",
        "imageId": "1",
        "name": "Litter 1kg",
        "price": 20,
        "unit": 9,
        "sold": 1,
      },
      {
        "id": "2",
        "imageId": "2",
        "name": "Cat Food",
        "price": 1.5,
        "unit": 8,
        "sold": 2
      },
    ]

    self.items = []

    # Table headers
    self.addLabel("ID", row=1, column=0, sticky="NSEW", font=("Verdana", 15))
    self.addLabel("Image", row=1, column=1, sticky="NSEW", font=("Verdana", 15))
    self.addLabel("Item Name", row=1, column=2, sticky="NSEW", font=("Verdana", 15))
    self.addLabel("Price (RM)", row=1, column=3, sticky="NSEW", font=("Verdana", 15))
    self.addLabel("Unit", row=1, column=4, sticky="NSEW", font=("Verdana", 15))
    self.addLabel("Sold Unit", row=1, column=5, sticky="NSEW", font=("Verdana", 15))

    # Table data
    start_row = 2
    self.imgs = []

    # Display each column of data in the table row-by-row
    for i in range(start_row, start_row + len(items)):
      item = items[i-start_row]
      item["id"] = self.addTextField(item["id"], row=i, column=0, sticky="NSEW", state="readonly", width=2)
      img = tk.PhotoImage(file=f"images/{item['imageId']}/100x100.png", height=100, width=100)
      item["image"] = self.addLabel("", row=i, column=1, sticky="NSEW")
      item["image"]["image"] = img
      self.imgs.append(img)
      item["name"] = self.addTextField(item["name"], row=i, column=2, sticky="NSEW", width=40)
      item["price"] = self.addFloatField(item["price"], row=i, column=3, sticky="NSEW", width=10, precision=2)
      item["unit"] = self.addIntegerField(item["unit"], row=i, column=4, sticky="NSEW", width=5)
      item["sold"] = self.addIntegerField(item["sold"], row=i, column=5, sticky="NSEW", state="readonly", width=5)
      self.items.append(item)

    self.addLabel("hello world", 0,0)


def main():
  ManagerDashboard().mainloop()


if __name__ == "__main__":
  main()
