from breezypythongui import EasyFrame, EasyPanel
import tkinter as tk
import tkinter.filedialog
from PIL import Image
from db import loadProducts, saveProducts, loadOrders, saveOrders
import os
import time


products = loadProducts()
orders = loadOrders()
font = ("Verdana", 10, "bold")

class ManagerDashboard(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, "Main Dashboard")
    self.master.attributes('-fullscreen', True)

    temp = orders.copy()
    temp.reverse()
    temp = list(filter(lambda x: not x["status"], temp))
    self.setBackground("#3f3a3c")

    start_row = 1
    self.sidePanel = self.addPanel(0, 0, rowspan=len(orders)+start_row, background="white")
    self.sidePanel.addButton("Manage Products", 1, 0, rowspan=2, command=self.manageProducts)
    self.sidePanel.addButton("Analytics", 3, 0, command=self.analytics)
    self.img = self.sidePanel.addLabel("", 0, 0, sticky="NSEW")
    img = tk.PhotoImage(file="images/cat logo200x200transparent.png", height=200, width=200)
    self.img["image"] = img
    self.imgs = [img]

    if len(temp) == 0:
      self.addLabel("There are no orders currently.", 0, 1, sticky="NSEW", background="#3f3a3c", foreground="white")
      return

    self.addLabel("Order ID", 0, 1, sticky="NES", background="#3f3a3c", foreground="white")
    self.addLabel("Datetime", 0, 2, sticky="NEWS", background="#3f3a3c", foreground="white")
    self.addLabel("Product", 0, 3, sticky="NEWS", background="#3f3a3c", foreground="white")
    self.addLabel("Quantity", 0, 4, sticky="NEWS", background="#3f3a3c", foreground="white")
    self.addLabel("Price", 0, 5, sticky="NEWS", background="#3f3a3c", foreground="white")
    self.addLabel("Total Price", 0, 6, sticky="NEWS", background="#3f3a3c", foreground="white")
    self.addLabel("Action", 0, 7, sticky="NEWS", background="#3f3a3c", foreground="white")

    for i in range(len(temp)):
      order = temp[i]
      j = i + start_row
      product = list(filter(lambda x: x["id"] == order["productId"], products))[0]
      # text = f"Order#{order['id']}\nDatetime: {order['datetime']}\nTotal Price: RM{'%.2f' % (order['price']*order['quantity'])}\nProduct: {product['name']}"
      self.addLabel(order["id"], j, 1, sticky="NSE", background="#3f3a3c", foreground="white")
      self.addLabel(order["datetime"], j, 2, sticky="NSEW", background="#3f3a3c", foreground="white")
      self.addLabel(order["productId"], j, 3, sticky="NSEW", background="#3f3a3c", foreground="white")
      self.addLabel(order["quantity"], j, 4, sticky="NSEW", background="#3f3a3c", foreground="white")
      self.addLabel(order["price"], j, 5, sticky="NSEW", background="#3f3a3c", foreground="white")
      self.addLabel(f"RM{'%.2f' % (order['price']*order['quantity'])}", j, 6, sticky="NSEW", background="#3f3a3c", foreground="white")
      self.addButton("Deliver", j, 7, command=lambda pos=i: self.deliver(pos)).config(foreground="white", background="gray")

  def deliver(self, pos):
    orders[pos]["status"] = True
    saveOrders(orders)
    self.master.destroy()
    ManagerDashboard().mainloop()

  def manageProducts(self):
    self.master.destroy()
    ProductManagement().mainloop()

  def analytics(self):
    self.master.destroy()
    Analytics()


class Analytics(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, "Analytics")
    self.master.attributes('-fullscreen', True)

    # Preprocess data
    temp = products.copy()
    hottest_item = max(products, key=lambda k: k["sold"])
    highest_ratings = max(products, key=lambda k: k["totalStars"])

    self.addLabel("Hottest Product", 0, 0, sticky="NSEW")
    self.img1 = self.addLabel("", 1, 0, sticky="NSEW")
    temp = tk.PhotoImage(file=f'image_db/{hottest_item["imageId"]}/200x200.png')
    self.img1["image"] = temp
    self.imgs = [temp]
    self.addLabel(hottest_item["name"], 2, 0, sticky="NSEW")

    self.addLabel("Highest Ratings", 0, 1, sticky="NSEW")
    self.img2 = self.addLabel("", 1, 1, sticky="NSEW")
    temp2 = tk.PhotoImage(file=f'image_db/{highest_ratings["imageId"]}/200x200.png')
    self.img2["image"] = temp2
    self.imgs.append(temp2)
    self.addLabel(highest_ratings["name"], 2, 1, sticky="NSEW")

  def __del__(self):
    ManagerDashboard().mainloop()


class ProductManagement(EasyFrame, tk.Toplevel):
  
  def __init__(self, pagination=0, search=""):
    EasyFrame.__init__(self, "Product Manager")
    self.master.attributes('-fullscreen', True)

    self.page = pagination
    self.imgs = []  # used to store image_db reference because if not stored, it will get destroyed from memory
    self.shopLogo = self.addLabel("", row=0, column=0, columnspan=2, sticky="NSEW")
    logo = tk.PhotoImage(file="cat logo200x200.png", width=200, height=200)
    self.shopLogo["image"] = logo
    self.imgs.append(logo)

    # Add button
    self.search = self.addTextField(search, row=0, column=2, columnspan=2, sticky="EW", width=25)
    self.addButton("Search", row=0, column=4, command=self.searchProduct)
    self.addButton("(+) Add Product", row=0, column=7, columnspan=1, command=self.add).config(font=font, background="#ee9b61", activebackground="white")
    
    global products

    temp = products.copy()
    if search != "":
      temp = list(filter(lambda x: search.lower() in x["name"].lower(), products))

    if len(temp) == 0:
      self.addLabel("No products yet. Add new product by pressing the button.", 1, 0, columnspan=7, sticky="NEW")
      return
    elif len(temp) <= 5:
      temp = temp[0: len(temp)]
    elif pagination == 0:
      temp = temp[0:5]
      page = self.page
      self.addButton(">", row=0, column=6, command=lambda page=page: self.pagination(page+1))
    elif pagination*5+5 >= len(temp):
      temp = temp[pagination*5:len(temp)]
      page = self.page
      self.addButton("<", row=0, column=5, command=lambda page=page: self.pagination(page-1))
    else:
      temp = temp[pagination*5:pagination*5+5]
      page = self.page
      self.addButton("<", row=0, column=5, command=lambda page=page: self.pagination(page-1))
      self.addButton(">", row=0, column=6, command=lambda page=page: self.pagination(page+1))

    # Table headers
    self.addLabel("ID", row=1, column=0, sticky="NSEW", font=font)
    self.addLabel("Image", row=1, column=1, sticky="NSEW", font=font)
    self.addLabel("Item Name", row=1, column=2, sticky="NSEW", font=font)
    self.addLabel("Price (RM)", row=1, column=3, sticky="NSEW", font=font)
    self.addLabel("Unit", row=1, column=4, sticky="NSEW", font=font)
    self.addLabel("Sold Unit", row=1, column=5, sticky="NSEW", font=font)
    self.addLabel("Actions", row=1, column=6, columnspan=2, sticky="NSEW", font=font)

    # Display each column of data in the table row-by-row
    self.start_row = 3
    self.shift_amount = 0
    background_picker = lambda n: "#f3c59d" if n % 2 == 0 else "#ee9b62"
    for i in range(self.start_row, self.start_row + len(temp)):
      bg = background_picker(i-self.start_row)
      product: dict = temp[(i-self.start_row)]
      img = tk.PhotoImage(file=f"image_db/{product['imageId']}/75x75.png", height=75, width=75)
      self.addButton("Edit", row=i, column=6, command=lambda item=product: self.edit(item)).configure(font=font, background=bg)
      self.addButton("Delete", row=i, column=7, command=lambda item=product: self.delete(item)).configure(font=font, background=bg)
      self.addLabel(product["id"], row=i, column=0, sticky="NSEW", background=bg)
      img_label = self.addLabel("", row=i, column=1, sticky="NSEW")
      img_label["image"] = img
      self.imgs.append(img)
      self.addLabel(product["name"], row=i, column=2, sticky="NSEW", font=font, background=bg)
      price =  "" if str(product["price"]) == "" else "%.2f" % product["price"]
      self.addLabel(price, row=i, column=3, sticky="NSEW", font=font, background=bg)
      self.addLabel(product["unit"], row=i, column=4, sticky="NSEW", font=font, background=bg)
      self.addLabel(product["sold"], row=i, column=5, sticky="NSEW", font=font, background=bg)
  
  def __del__(self):
    ManagerDashboard().mainloop()

  def edit(self, item):
    ProductEditMenu(self, item)

  def add(self):
    ProductEditMenu(self)

  def searchProduct(self):
    self.master.destroy()
    ProductManagement(search=self.search.getText(), pagination=0)

  def pagination(self, number):
    self.master.destroy()
    ProductManagement(search=self.search.getText(), pagination=number)

  def delete(self, item):
    products.pop(products.index(item))
    saveProducts(products)
    self.master.destroy()
    ProductManagement()


class ProductEditMenu(EasyFrame, tk.Toplevel):
  def __init__(self, parent, product=None):

    title = "Add Product"
    if not product:
      product = {
      "id": str(int(products[-1]["id"])+1),
      "imageId": "",
      "name": "",
      "price": 0,
      "unit": 0,
      "sold": 0,
      "type": "food"
      }
    else:
      title = f"Edit Product#{product['id']}"

    # Init window
    EasyFrame.__init__(self, title)
    tk.Toplevel.__init__(self)

    # Store position, item, parent, and image
    try:
      self.pos = products.index(product)
    except ValueError:
      self.pos = -1
    self.item = product
    self.parent = parent
    self.img_temp = []

    # Product image
    self.editImage = self.addLabel("", row=0, column=0, sticky="NSEW")
    try:
      img = tk.PhotoImage(file=f"image_db/{product['imageId']}/200x200.png", width=200, height=200)
    except:
      img = ""

    self.editImage["image"] = img
    self.img_temp.append(img)
    self.uploadButton = self.addButton("Upload Image", row=1, column=0, columnspan=2, command=self.uploadImage)
    self.newImagePath = ""

    # Product ID
    self.addLabel("Product ID", row=2, column=0)
    self.editId = self.addTextField(product["id"], row=3, column=0, sticky="W", state="disabled", width=5)

    # Product name
    self.addLabel("Name", row=4, column=0)
    self.editName = self.addTextField(product["name"], row=5, column=0, width=50, sticky="W")

    # Product price
    self.addLabel("Price (RM)", row=6, column=0)
    self.editPrice = self.addFloatField("%.2f" % product["price"], row=7, column=0, precision=2, sticky="W")

    # Product unit
    self.addLabel("Unit", row=8, column=0)
    self.editUnit = self.addIntegerField(product["unit"], row=9, column=0, sticky="W")

    # Types
    self.types = self.addRadiobuttonGroup(10, 0, rowspan=4)
    food = self.types.addRadiobutton("Food")
    if product["type"] == "food":
      self.types.setSelectedButton(food)
    medicine = self.types.addRadiobutton("Medicine")
    if product["type"] == "medicine":
      self.types.setSelectedButton(medicine)
    hygiene = self.types.addRadiobutton("Hygiene")
    if product["type"] == "hygiene":
      self.types.setSelectedButton(hygiene)
    toys = self.types.addRadiobutton("Toys")
    if product["type"] == "toys":
      self.types.setSelectedButton(toys)

    # Save Button
    self.save = self.addButton("Save", row=14, column=0, command=self.save)

  def uploadImage(self):
    # Get image file
    fList = [("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
    filePath = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)

    # Validate image file data
    if len(filePath) == 0:
      self.messageBox("Empty filename", message="Please upload file again")
      return
    
    self.newImagePath = filePath
    
    # Create temporary image for review purpose
    with Image.open(filePath) as tempImg:
      # Store image temporarily under `temp` folder
      tempImg = tempImg.resize((200, 200))
      tempFile = f"temp/{time.time()}.png"
      tempImg.save(tempFile)

    # Replace picture
    tempImg = tk.PhotoImage(file=tempFile, width=200, height=200)
    self.editImage["image"] = tempImg
    self.img_temp.append(tempImg)
    self.uploadButton["state"] = "disabled"

  @staticmethod
  def getNewImageId():
    # Specify the directory path
    directory_path = "image_db"

    # Get the list of files and directories in the specified directory
    files_and_directories = os.listdir(directory_path)

    # Filter out only the directories from the list
    directories = [item for item in files_and_directories if os.path.isdir(os.path.join(directory_path, item))]
    directories.remove("[imageId]")
    return max([int(x) for x in directories])+1

  def save(self):
    # Validate name
    name = self.editName.getText()
    if len(name) == 0:
      self.messageBox("Empty Name", message="Product name cannot be empty")
      return
    self.item["name"] = name
    
    # Validate price
    try:
      price = self.editPrice.getNumber()
    except ValueError:
      self.messageBox("Invalid Price", message="Product price must be a positive number or zero")
      return
    self.item["price"] = price
    
    # Validate unit
    try:
      unit = self.editUnit.getNumber()
    except ValueError:
      self.messageBox("Invalid Unit", message="Product unit must be a positive integer or zero")
      return
    self.item["unit"] = unit

    # Validate image update, if any
    if len(self.newImagePath) > 0:
      newImageId = self.getNewImageId()
      os.makedirs(f"image_db/{newImageId}")

      # Preprocess image_db
      with Image.open(self.newImagePath) as img:
        img.save(f"image_db/{newImageId}/original.png")
        img_1 = img.resize((200, 200))
        img_1.save(f"image_db/{newImageId}/200x200.png")
        img_2 = img.resize((100, 100))
        img_2.save(f"image_db/{newImageId}/100x100.png")
        img_3 = img.resize((100, 100))
        img_3.save(f"image_db/{newImageId}/75x75.png")
        img_4 = img.resize((75, 75))
        img_4.save(f"image_db/{newImageId}/50x50.png")
      self.item["imageId"] = newImageId
    elif self.item["imageId"] == "":
      self.messageBox("Invalid Image", message="Please upload an image for this product")
      return
    
    # Update type
    self.item["type"] = self.types.getSelectedButton()["text"].lower()

    # Save the new update
    if self.pos == -1:
      products.append(self.item)
    else:
      products[self.pos] = self.item
    saveProducts(products)
    self.parent.master.destroy()
    ProductManagement()


def main():
  ManagerDashboard().mainloop()


if __name__ == "__main__":
  main()
