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

        # Shop title
        textLabel1 = self.addLabel(text="Pawsome Pet Shop Homepage", row=0, column=0, columnspan=4, font=('Microsoft YaHei UI Light',23,'bold'), sticky="NSEW")
        self.setBackground("white")
        
        # Food catalogue
        imageLabel1 = self.addLabel(text="", row=1, column=0, sticky="NSEW")
        textLabel1 = self.addLabel(text="FOOD", row=2, column=0, sticky="NSEW")
        self.image1 = PhotoImage(file="images/1.gif")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"
        self.buyFood = self.addButton(text="food catalouge", row=3, column=0, command = self.showFood)

        # Medicine catalogue
        imageLabel2 = self.addLabel(text="", row=1, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="MEDICINE", row=2, column=1, sticky="NSEW")
        self.image2 = PhotoImage(file="images/2.gif")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"
        self.buyMed = self.addButton(text="medicine catalouge", row=3, column=1, command = self.showMed)

        # Hygiene catalogue
        imageLabel3 = self.addLabel(text="", row=1, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="HYGIENE", row=2, column=2, sticky="NSEW")
        self.image3 = PhotoImage(file="images/3.gif")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"
        self.buyHygiene = self.addButton(text="hygiene catalouge", row=3, column=2, command = self.showHygiene)

        # Toys catalogue
        imageLabel4 = self.addLabel(text="", row=1, column=3, sticky="NSEW")
        textLabel4 = self.addLabel(text="TOYS", row=2, column=3, sticky="NSEW")
        self.image4 = PhotoImage(file="images/4.gif")
        imageLabel4["image"] = self.image4
        font4 = Font(family="Verdana", size=20, slant="italic")
        textLabel4["font"] = font4
        textLabel4["foreground"] = "#57a1f8"
        self.buyToys = self.addButton(text="toys catalouge", row=3, column=3, command = self.showToys)

    def showFood(self):
        self.master.destroy()
        ShowProducts(type="food")
            
    def showMed(self):
        self.master.destroy()
        ShowProducts(type="medicine")

    def showHygiene(self): 
        self.master.destroy()
        ShowProducts(type="hygiene")

    def showToys(self):
        self.master.destroy()
        ShowProducts(type="toys")


class ShowProducts(EasyFrame):
    def __init__(self, type, pagination=0):
        """General class to display products. Products can be specified by providing `types` parameter."""

        # Setup window
        EasyFrame.__init__(self, title="FOOD CATALOGUE")
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
        self.panel = self.addPanel(8, 0, columnspan=3, background="orange")
        self.panel.nextpage = self.addButton(text="Checkout Receipt", row=8, column=0, columnspan=2, command=self.checkout)
        self.panel.back = self.addButton(text="Back to Homepage", row=8, column=1, columnspan=2, command = self.goback)
        
        self.imgs = []  # Temporary array to keep images in memory so that it is not lost
        i = 0
        # Display products
        for r in range(0, 4, 3):
            for c in range(3):
                try:
                    # When index exceeded, break the loop
                    product = product_temp[i]
                except IndexError:
                    break
                imgLabel = self.addLabel("", r, c, sticky="NESW")
                self.addLabel(product["name"], r+1, c, sticky="NEWS", font=("Verdana", 20, "italic"), foreground="#57a1f8")
                img = PhotoImage(file=f"image_db/{product['imageId']}/200x200.png")
                imgLabel["image"] = img
                self.imgs.append(img)
                self.addButton("View product", r+2, c, command=lambda item=product: self.addToCart(item))
                i += 1
    
    def pagination(self, page):
        self.master.destroy()
        ShowProducts(type=self.type, pagination=page)

    def addToCart(self, item):
        ViewProduct(item)
    
    def checkout(self):
        Checkout()

    def goback(self):
        self.master.destroy()
        shopCatalogue().mainloop()


class ViewProduct(EasyFrame, Toplevel):
    def __init__(self, item):

        # Setup window
        EasyFrame.__init__(self, "View Products")
        Toplevel.__init__(self)
        self.setBackground("white")

        # Image
        self.img = self.addLabel("", 0, 0, columnspan=2)
        img = PhotoImage(file=f"image_db/{item['imageId']}/200x200.png")
        self.img["image"] = img
        self.imgs = [img]

        # Properties of product
        self.addLabel(item["name"], 1, 0, sticky="NESW", columnspan=2)
        self.addLabel("Stocks Available:", 2, 0, sticky="NES")
        self.addLabel(f"{item['unit']} unit", 2, 1, sticky="NEW")
        self.addLabel("Price:", 3, 0, sticky="NES")
        self.addLabel(f"{'RM%.2f' % item['price']}", 3, 1, sticky="NEW")
        self.addLabel("Quantity:", 4, 0, sticky="ENS")
        quantity = Cart.get(item["id"], {"quantity": 0})["quantity"]
        self.quantity = self.addIntegerField(quantity, 4, 1)
        self.addButton("Add to cart", 5, 0, command=lambda item=item: self.saveInCart(item), columnspan=2)

    def saveInCart(self, item):
        quantity = self.quantity.getNumber()

        if quantity > item['unit']:
            self.messageBox('Not enough products', 'Not enough unit available right now')
            return

        Cart[item["id"]] = item
        item["quantity"] = quantity
        self.destroy()


class Checkout(EasyFrame, Toplevel):
    def __init__(self):
        EasyFrame.__init__(self)
        Toplevel.__init__(self)

        self.geometry("400x400")
        self.config(background="sky blue")

        # Display receipt header
        header_label = Label(self, text="--- PAWSOME PURCHASE RECEIPT ---", bg="sky blue")
        header_label.pack(side=TOP)

        total_cost = 0

        # Create a frame to display the receipt in a table-like format
        receipt_frame = Frame(self, bg="sky blue")
        receipt_frame.pack(fill=BOTH, expand=True)

        # Display table headers
        headers = ["NAME", "PRICE", "UNIT", "TOTAL"]
        for i, header in enumerate(headers):
            header_label = Label(receipt_frame, text=header, bg="sky blue")
            header_label.grid(row=0, column=i, padx=5, pady=5)

        overall_cost = 0
        # Display each product in a row
        for no, k in enumerate(Cart.keys()):
            order = Cart[k]
            name = order['name']
            price = order['price']
            quantity = order['quantity']
            total = price * quantity
            total_cost += total

            # Display product details in corresponding columns
            product_details = [name, f"${price:.2f}", quantity, f"${total:.2f}"]
            for col, detail in enumerate(product_details):
                detail_label = Label(receipt_frame, text=detail, bg="sky blue")
                detail_label.grid(row=no + 1, column=col, padx=5, pady=5)

            overall_cost += total_cost

        # Display total cost
        total_label = Label(self, text=f"Total cost: ${(overall_cost):.2f}\n10 % tax: ${overall_cost*.1:.2f}\nOverall cost = ${overall_cost*1.1:.2f}\nThank you for purchasing with us!", bg="sky blue")
        total_label.pack()  

        # Button to open the star rating window
        rating_button = Button(self, text="Give Rating", command=self.open_rating_window)
        rating_button.pack(pady=10)

    def open_rating_window(self):
        rating_window = Toplevel()
        rating_window.title("Give Rating")

        # Create and pack the StarRating widget in the rating window
        rating_frame = StarRating(rating_window, numStars=5, callback=lambda rating: self.on_rating_submit(rating))
        rating_frame.pack(pady=20)

    def on_rating_submit(self, rating):
        print("You rated:", self)

        # Close the parent window (receipt window)
        self.destroy()

    def pay(self):
        self.messageBox("Payment Successful!", message="Thank you for ordering with us! Your order is on its way ^..^")
        self.master.destroy()

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()


from tkinter import *
from starRating import StarRating  # Import your StarRating class from the starRating module

def receipt():
    top = Toplevel()
    top.geometry("400x400")
    top.config(background="sky blue")

    # Display receipt header
    header_label = Label(top, text="--- PAWSOME PURCHASE RECEIPT ---", bg="sky blue")
    header_label.pack(side=TOP)

    orders = [
        {"company": "Whiskas", "name": "Dry Food", "price": 10.0, "unit": 2, "total": 20.0},
        {"company": "Royal Canin", "name": "Dry Food", "price": 15.0, "unit": 3, "total": 45.0},
        {"company": "Snappy Tom", "name": "Wet Food", "price": 20.0, "unit": 1, "total": 20.0}
    ]

    total_cost = 0

    # Create a frame to display the receipt in a table-like format
    receipt_frame = Frame(top, bg="sky blue")
    receipt_frame.pack(fill=BOTH, expand=True)

    # Display table headers
    headers = ["NAME", "PRICE", "UNIT", "TOTAL"]
    for i, header in enumerate(headers):
        header_label = Label(receipt_frame, text=header, bg="sky blue")
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display each product in a row
    for idx, order in enumerate(orders):
        name = order['name']
        price = float(order['price'])
        unit = int(order['unit'])
        total = price * unit
        total_cost += total

        # Display product details in corresponding columns
        product_details = [name, f"${price:.2f}", unit, f"${total:.2f}"]
        for col, detail in enumerate(product_details):
            detail_label = Label(receipt_frame, text=detail, bg="sky blue")
            detail_label.grid(row=idx + 1, column=col, padx=5, pady=5)

    tax = 0.1 * total_cost
    overall_cost = tax + total_cost

    # Display total cost
    total_label = Label(top, text=f"Total cost: ${(overall_cost - tax):.2f}\n10 % tax: ${tax:.2f}\nOverall cost = ${overall_cost}\nThank you for purchasing with us!", bg="sky blue")
    total_label.pack()

    # Button to open the star rating window
    rating_button = Button(top, text="Give Rating", command=lambda: open_rating_window(top))
    rating_button.pack(pady=10)

def open_rating_window(parent):
    rating_window = Toplevel()
    rating_window.title("Give Rating")

    # Create and pack the StarRating widget in the rating window
    rating_frame = StarRating(rating_window, numStars=5, callback=lambda rating: on_rating_submit(rating, parent))
    rating_frame.pack(pady=20)

def on_rating_submit(rating, parent):
    print("You rated:", rating)

    # Close the parent window (receipt window)
    parent.destroy()

        
def main():
    shopCatalogue().mainloop()


if __name__=="__main__":
    main()
