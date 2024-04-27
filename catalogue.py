"""
Program: catalogue.py
Author: Murfiqah, Khilfi, Zainatul
Main view for the user to buy items from the shop.
"""

from breezypythongui import EasyFrame
from tkinter import *
from tkinter.font import Font
from db import loadSession, loadProducts


# Global variables to store products, user ID, cart number, and cart items
Products = loadProducts()
UID, CARTNUMBER = loadSession()
Cart = {}

# Global variables to store screen dimensions
root = Tk()
SCREEN_WIDTH, SCREEN_HEIGHT = 2560, 1440
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")


class shopCatalogue(EasyFrame):
    """Parent catalogue view showing all types of items sold by this shop."""

    def __init__(self):
        EasyFrame.__init__(self, "homepage", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.master.geometry(f"{SCREEN_HEIGHT}x{SCREEN_WIDTH}")
        # Shop title
        textLabel1 = self.addLabel(text="Pawsome Pet Shop Homepage",\
                                   row=0, column=0,columnspan=4,\
                                   font=('Microsoft YaHei UI Light',23,'bold'),\
                                   sticky="NSEW")
        self.setBackground("white")
        
        # Food catalogue
        imageLabel1 = self.addLabel(text="", row=1, column=0, sticky="NSEW")
        textLabel1 = self.addLabel(text="FOOD", row=2, column=0,\
                                   sticky="NSEW")
        self.image1 = PhotoImage(file="images/1.gif")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"
        self.buyFood = self.addButton(text="food catalouge", row=3, column=0, command = self.showFood)

        # Medicine catalogue
        imageLabel2 = self.addLabel(text="", row=1, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="MEDICINE", row=2, column=1,\
                                   sticky="NSEW")
        self.image2 = PhotoImage(file="images/2.gif")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"
        self.buyMed = self.addButton(text="medicine catalouge", row=3, column=1, command = self.showMed)

        # Hygiene catalogue
        imageLabel3 = self.addLabel(text="", row=1, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="HYGIENE", row=2, column=2,\
                                   sticky="NSEW")
        self.image3 = PhotoImage(file="images/3.gif")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"
        self.buyHygiene = self.addButton(text="hygiene catalouge", row=3, column=2, command = self.showHygiene)

        # Toys catalogue
        imageLabel4 = self.addLabel(text="", row=1, column=3, sticky="NSEW")
        textLabel4 = self.addLabel(text="TOYS", row=2, column=3,\
                                   sticky="NSEW")
        self.image4 = PhotoImage(file="images/4.gif")
        imageLabel4["image"] = self.image4
        font4 = Font(family="Verdana", size=20, slant="italic")
        textLabel4["font"] = font4
        textLabel4["foreground"] = "#57a1f8"
        self.buyToys = self.addButton(text="toys catalouge", row=3, column=3, command = self.showToys)


    def showFood(self):
        self.master.destroy()
        showProducts(type="food")
            
    def showMed(self):
        self.master.destroy()
        showProducts(type="medicine")

    def showHygiene(self): 
        self.master.destroy()
        showProducts(type="hygiene")

    def showToys(self):
        self.master.destroy()
        showProducts(type="toys")


class showProducts(EasyFrame):
    def __init__(self, type, pagination=0):
        """General class to display products. Products can be specified by providing `types` parameter."""

        # Setup window
        EasyFrame.__init__(self,title="FOOD CATALOGUE")
        self.master.attributes("-fullscreen", True)
        self.setBackground("white")
        
        # Cache the item type
        self.type = type

        # Temporary product list
        product_temp = list(filter(lambda x: x["type"] == type, Products))

        # Display different UI based on the number of product and pagination number
        if len(product_temp) == 0:
            self.addLabel("No products found.", 1, 0, columnspan=3, rowspan=2, sticky="NSEW")
        elif len(product_temp) <= 6:
            product_temp = product_temp[0: len(product_temp)]
        elif pagination == 0:
            product_temp = product_temp[0:6]
            self.addButton(">", row=6, column=2, command=lambda page=pagination: self.pagination(page+1))
        elif pagination*6+6 >= len(product_temp):
            product_temp = product_temp[pagination*6:len(product_temp)]
            self.addButton("<", row=6, column=0, command=lambda page=pagination: self.pagination(page-1))
        else:
            product_temp = product_temp[pagination*6:pagination*6+6]
            self.addButton("<", row=7, column=0, command=lambda page=pagination: self.pagination(page-1))
            self.addButton(">", row=7, column=2, command=lambda page=pagination: self.pagination(page+1))
        
        # Navigation buttons
        self.nextpage = self.addButton(text="Checkout",row=8,column=0,columnspan=2, command=self.checkout)
        self.back = self.addButton(text="Back to Homepage", row=8, column=2, columnspan=1, command = self.goback)
        
        self.imgs = []  # Temporary array to keep images in memory so that it is not lost
        i = 0
        # Display products
        for r in range(0, 4, 3):
            for c in range(3):
                try:
                    product = product_temp[i]
                except IndexError:
                    break
                imgLabel = self.addLabel("", r, c, sticky="NESW")
                self.addLabel(product["name"], r+1, c, sticky="NEWS", font=("Verdana", 20, "italic"), foreground="#57a1f8")
                img = PhotoImage(file=f"image_db/{product['imageId']}/200x200.png")
                imgLabel["image"] = img
                self.imgs.append(img)
                self.addButton("View Product", r+2, c, command=lambda item=product: self.addToCart(item))
                i += 1
    
    def pagination(self, page):
        self.master.destroy()
        showProducts(type=self.type, pagination=page)

    def addToCart(self, item):
        ViewProduct(item)
    
    def checkout(self):
        Checkout()

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()


class ViewProduct(EasyFrame, Toplevel):
    def __init__(self, item):
        EasyFrame.__init__(self, "View Products")
        Toplevel.__init__(self)
        self.setBackground("white")

        self.img = self.addLabel("", 0, 0, columnspan=2)
        img = PhotoImage(file=f"image_db/{item['imageId']}/200x200.png")
        self.img["image"] = img
        self.imgs = [img]

        self.addLabel(item["name"], 1, 0, sticky="NESW", columnspan=2)
        self.addLabel("Price:", 2, 0, sticky="NES")
        self.addLabel(f"{'RM%.2f' % item['price']}", 2, 1, sticky="NEWS")
        # self.addLabel("Rating:", 3, 0, sticky="NES")
        # self.addLabel(f'{item["totalStars"] / item["sold"]} / 5')
        self.addLabel("Quantity:", 3, 0, sticky="ENS")
        quantity = Cart.get(item["id"], {"quantity": 0})["quantity"]
        self.quantity = self.addIntegerField(quantity, 3, 1)

        self.addButton("Buy", 4, 0, command=lambda item=item: self.saveInCart(item), columnspan=2)

    def saveInCart(self, item):
        Cart[item["id"]] = item
        item["quantity"] = self.quantity.getNumber()
        self.destroy()


class Checkout(EasyFrame, Toplevel):
    def __init__(self):
        EasyFrame.__init__(self)
        Toplevel.__init__(self)
        self.addLabel("--- PAWSOME PURCHASE RECEIPT ---", 0, 0)
        self.setBackground("sky blue")
        
        format = "%20s | RM%.2f | %4s | RM%.2f"
        text = "%20s | %6s | %4s | R%6s" % ("NAME", "PRICE", "UNIT", "TOTAL") + '\n'
        total = 0
        for v in Cart.values():
            text += format % (v["name"], v["price"], v["quantity"], v["price"] * v["quantity"]) + '\n'
            total += v["price"] * v["quantity"]


        self.addTextArea(text, 1, 0)
        self.addLabel(f"Price: RM{'%.2f'%total}", 2, 0)
        self.addButton("Pay", command=self.pay, row=3, column=0)

    def pay(self):
        self.messageBox("Payment Successful!", message="Thank you for ordering with us! Your order is on its way ^..^")
        self.master.destroy()

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()

        
def main():
    shopCatalogue().mainloop()


if __name__=="__main__":
    main()
