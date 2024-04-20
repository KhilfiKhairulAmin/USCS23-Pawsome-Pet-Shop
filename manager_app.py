from breezypythongui import EasyFrame
import tkinter as tk
from db import loadOrders, loadProducts


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

    self.items = loadProducts()

    # Table headers
    self.addLabel("ID", row=1, column=0, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Image", row=1, column=1, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Item Name", row=1, column=2, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Price (RM)", row=1, column=3, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Unit", row=1, column=4, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Sold Unit", row=1, column=5, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Actions", row=1, column=6, columnspan=2, sticky="NSEW", font=("Verdana", 10))

    # Display each column of data in the table row-by-row
    self.imgs = []  # used to store images reference because if not stored, it will get destroyed at the end of the for loop
    start_row = 2
    for i in range(start_row, start_row + len(self.items)):
      item = self.items[i-start_row]
      self.addLabel(item["id"], row=i, column=0, sticky="NSEW")
      img = tk.PhotoImage(file=f"images/{item['imageId']}/original.png", height=50, width=50)
      img_label = self.addLabel("", row=i, column=1, sticky="NSEW")
      img_label["image"] = img
      self.imgs.append(img)
      self.addLabel(item["name"], row=i, column=2, sticky="NSEW")
      self.addLabel("%.2f" % item["price"], row=i, column=3, sticky="NSEW")
      self.addLabel(item["unit"], row=i, column=4, sticky="NSEW")
      self.addLabel(item["sold"], row=i, column=5, sticky="NSEW")
      self.addButton("Edit", row=i, column=6, command=lambda: self.edit(i))

    self.addLabel("hello world", 0,0)

  def edit(self, i):
    pass

  def add(self):
    pass

  def delete(self):
    pass


def main():
  ManagerDashboard().mainloop()


if __name__ == "__main__":
  main()
