from breezypythongui import EasyFrame
import tkinter as tk
import tkinter.filedialog
from PIL import Image
from db import loadProducts, saveProducts
import os
import time


products = loadProducts()
font = ("Verdana", 10)


class ManagerDashboard(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, "Main Dashboard")
    self.addButton("Manage Products", 0, 0, command=self.manageProducts)

  def manageProducts(self):
    self.master.destroy()
    ProductManagement().mainloop()


class ProductManagement(EasyFrame):
  
  def __init__(self, pagination=0):
    EasyFrame.__init__(self, "Product Manager")

    self.imgs = []  # used to store images reference because if not stored, it will get destroyed from memory
    self.shopLogo = self.addLabel("", row=0, column=0, sticky="NSEW")
    logo = tk.PhotoImage(file="cat logo100x100.png")
    self.shopLogo["image"] = logo
    self.imgs.append(logo)

    # Add button
    self.addButton("(+) Add Product", row=0, column=1, columnspan=2, command=self.add).config(font=font, background="#ee9b61", activebackground="white")
    self.addLabel("Search", )
    self.search = self.addTextField("", row=0, column=6, columnspan=3)
    if len(products) == 0:
      self.addLabel("No products yet. Add new product by pressing the button.", 1, 0, columnspan=7)
      return

    # Table headers
    self.addLabel("ID", row=1, column=0, sticky="SEW", font=font)
    self.addLabel("Image", row=1, column=1, sticky="NSEW", font=font)
    self.addLabel("Item Name", row=1, column=2, sticky="NSEW", font=font)
    self.addLabel("Price (RM)", row=1, column=3, sticky="NSEW", font=font)
    self.addLabel("Unit", row=1, column=5, sticky="NSEW", font=font)
    self.addLabel("Sold Unit", row=1, column=5, sticky="NSEW", font=font)
    self.addLabel("Actions", row=1, column=6, columnspan=2, sticky="NSEW", font=font)

    # Display each column of data in the table row-by-row
    self.start_row = 3
    self.shift_amount = 0
    background_picker = lambda n: "#f3c59d" if n % 2 == 0 else "#ee9b62"
    for i in range(self.start_row, self.start_row + 10):
      bg = background_picker(i-self.start_row)
      product: dict = products[i-self.start_row]
      self.addLabel(product["id"], row=i, column=0, sticky="NSEW", background=bg)
      img = tk.PhotoImage(file=f"images/{product['imageId']}/100x100.png", height=50, width=50)
      img_label = self.addLabel("", row=i, column=1, sticky="NSEW")
      img_label["image"] = img
      self.imgs.append(img)
      self.addLabel(product["name"], row=i, column=2, sticky="NSEW", font=font, background=bg)
      self.addLabel("%.2f" % product["price"], row=i, column=3, sticky="NSEW", font=font, background=bg)
      self.addLabel(product["unit"], row=i, column=4, sticky="NSEW", font=font, background=bg)
      self.addLabel(product["sold"], row=i, column=5, sticky="NSEW", font=font, background=bg)
      self.addButton("Edit", row=i, column=6, command=lambda pos=i-self.start_row: self.edit(pos)).configure(font=font, background=bg)
      self.addButton("Delete", row=i, column=7, command=lambda pos=i-self.start_row: self.delete(pos)).configure(font=font, background=bg)

  def edit(self, item):
    ProductEditMenu(self, item)

  def add(self):
    ProductEditMenu(self, {
      "id": str(int(products[-1]["id"])+1),
      "imageId": "",
      "name": "",
      "price": 0,
      "unit": 0,
      "sold": 0
    })

  def delete(self, pos):
    def deleteProduct(pos):
      products.pop(pos)
      saveProducts(products)
      self.master.destroy()
      ProductManagement().mainloop()

    Modal("Delete Product", lambda pos=pos: deleteProduct(pos))


class ProductEditMenu(EasyFrame, tk.Toplevel):
  def __init__(self, parent, pos):
    title = "Add Product"
    try:
      # Get product at position `pos`
      product = products[pos]
      title = f"Edit Product#{product['id']}"
    except IndexError:
      # For add new product
      product = {
        "id": str(pos),
        "imageId": "",
        "name": "",
        "price": 0,
        "unit": 0,
        "sold": 0
      }

    # Init window
    EasyFrame.__init__(self, title)
    tk.Toplevel.__init__(self)

    # Store position, item, parent, and image
    self.pos = pos
    self.item = product
    self.parent = parent
    self.img_temp = []

    # Product image
    self.editImage = self.addLabel("", row=0, column=0, sticky="NSEW")
    try:
      img = tk.PhotoImage(file=f"images/{product['imageId']}/200x200.png", width=200, height=200)
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

    # Save Button
    self.save = self.addButton("Save", row=10, column=0, command=self.save)

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
    directory_path = "images"

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
      os.makedirs(f"images/{newImageId}")

      # Preprocess images
      with Image.open(self.newImagePath) as img:
        img.save(f"images/{newImageId}/original.png")
        img_1 = img.resize((200, 200))
        img_1.save(f"images/{newImageId}/200x200.png")
        img_2 = img.resize((100, 100))
        img_2.save(f"images/{newImageId}/100x100.png")
        img_3 = img.resize((50, 50))
        img_3.save(f"images/{newImageId}/50x50.png")

      self.item["imageId"] = newImageId
    elif self.item["imageId"] == "":
      self.messageBox("Invalid Image", message="Please upload an image for this product")
      return
    
    # Save the new update
    try:
      products[self.pos] = self.item
    except IndexError:
      products.append(self.item)
    saveProducts(products)
    self.parent.master.destroy()
    ProductManagement().mainloop()


class Modal(EasyFrame, tk.Toplevel):
  def __init__(self, title="", command=lambda : None):
    EasyFrame.__init__(self, title)
    tk.Toplevel.__init__(self)
    self.addLabel("Are you sure?", 0, 0, columnspan=2)
    self.addButton("Cancel", 1, 0)
    self.addButton("Yes", 1, 1, command=command)


def main():
  ManagerDashboard().mainloop()


if __name__ == "__main__":
  main()
