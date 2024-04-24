from breezypythongui import EasyFrame
import tkinter as tk
import tkinter.filedialog
from PIL import Image
from db import loadProducts, saveProducts
import os
import time


products = loadProducts()


class ManagerDashboard(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, "Main Dashboard")
    self.addButton("Manage Products", 0, 0, command=self.manageProducts)

  def manageProducts(self):
    self.master.destroy()
    ProductManagement().mainloop()


class ProductManagement(EasyFrame):
  
  def __init__(self):
    EasyFrame.__init__(self, "Product Manager")

    # Table headers
    self.addLabel("ID", row=1, column=0, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Image", row=1, column=1, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Item Name", row=1, column=2, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Price (RM)", row=1, column=3, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Unit", row=1, column=4, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Sold Unit", row=1, column=5, sticky="NSEW", font=("Verdana", 10))
    self.addLabel("Actions", row=1, column=6, columnspan=2, sticky="NSEW", font=("Verdana", 10))

    # Display each column of data in the table row-by-row
    self.imgs = []  # used to store images reference because if not stored, it will get destroyed from memory
    self.start_row = 2
    self.shift_amount = 0
    for i in range(self.start_row, self.start_row + len(products)):
      product: dict = products[i-self.start_row]
      self.addLabel(product["id"], row=i, column=0, sticky="NSEW")
      img = tk.PhotoImage(file=f"images/{product['imageId']}/50x50.png", height=50, width=50)
      img_label = self.addLabel("", row=i, column=1, sticky="NSEW")
      img_label["image"] = img
      self.imgs.append(img)
      self.addLabel(product["name"], row=i, column=2, sticky="NSEW")
      self.addLabel("%.2f" % product["price"], row=i, column=3, sticky="NSEW")
      self.addLabel(product["unit"], row=i, column=4, sticky="NSEW")
      self.addLabel(product["sold"], row=i, column=5, sticky="NSEW")
      self.addButton("Edit", row=i, column=6, command=lambda pos=i-self.start_row: self.edit(pos))
    self.addLabel("hello world", 0,0)

  def edit(self, pos):
    ProductEditMenu(self, pos)


class ProductEditMenu(EasyFrame, tk.Toplevel):
  def __init__(self, parent, pos):
    # Get product at position `pos`
    product = products[pos]

    # Init window
    EasyFrame.__init__(self, f"Edit Product#{product['id']}")
    tk.Toplevel.__init__(self)

    # Store position, item, parent, and image
    self.pos = pos
    self.item = product
    self.parent = parent
    self.img_temp = []

    # Product image
    self.editImage = self.addLabel("", row=0, column=0, sticky="NSEW")
    img = tk.PhotoImage(file=f"images/{product['imageId']}/200x200.png", width=200, height=200)
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
    self.editPrice = self.addFloatField(product["price"], row=7, column=0, precision=2, sticky="W")

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
    
    with Image.open(filePath) as tempImg:
      # Store image temporarily under `temp` folder
      tempImg = tempImg.resize((200, 200))
      tempFile = f"temp/{time.time()}.png"
      tempImg.save(tempFile)

    tempImg = tk.PhotoImage(tempFile, width=200, height=200)
    self.editImage = self.addLabel("", 0, 0)
    self.editImage["image"] = tempImg
    self.img_temp.append(tempImg)

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
    
    # Save the new update
    products[self.pos] = self.item
    saveProducts(products)
    self.parent.master.destroy()
    ProductManagement().mainloop()

def main():
  ManagerDashboard().mainloop()


if __name__ == "__main__":
  main()
