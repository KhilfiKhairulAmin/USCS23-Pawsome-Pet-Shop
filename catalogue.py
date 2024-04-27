import datetime
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import *
from db import loadSession

uid, cartNumber = loadSession()


class shopCatalogue (EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="homepage")
        self.master.attributes("-fullscreen", True)
        self.setBackground("white")

        textLabel1 = self.addLabel(text="Pawsome Pet Shop Homepage",\
                                   row=0, column=0,columnspan=4,\
                                   font=('Microsoft YaHei UI Light',23,'bold'),\
                                   sticky="NSEW")
        
        # image 1
        imageLabel1 = self.addLabel(text="", row=1, column=0, sticky="NSEW")
        textLabel1 = self.addLabel(text="FOOD", row=2, column=0,\
                                   sticky="NSEW")
        self.image1 = PhotoImage(file="1.gif")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"

        #image 2
        imageLabel2 = self.addLabel(text="", row=1, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="MEDICINE", row=2, column=1,\
                                   sticky="NSEW")
        self.image2 = PhotoImage(file="2.gif")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"

        #image 3
        imageLabel3 = self.addLabel(text="", row=1, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="HYGIENE", row=2, column=2,\
                                   sticky="NSEW")
        self.image3 = PhotoImage(file="3.gif")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"

        #image 4
        imageLabel4 = self.addLabel(text="", row=1, column=3, sticky="NSEW")
        textLabel4 = self.addLabel(text="TOYS", row=2, column=3,\
                                   sticky="NSEW")
        self.image4 = PhotoImage(file="4.gif")
        imageLabel4["image"] = self.image4
        font4 = Font(family="Verdana", size=20, slant="italic")
        textLabel4["font"] = font4
        textLabel4["foreground"] = "#57a1f8"

        #button
        self.buyFood = self.addButton(text="food catalouge",row=3,column=0,\
                                   command = self.showFood)
        self.buyMed = self.addButton(text="medicine catalouge",row=3,column=1,\
                                   command = self.showMed)
        self.buyHygiene = self.addButton(text="hygiene catalouge",row=3,column=2,\
                                   command = self.showHygiene)
        self.buyToys = self.addButton(text="toys catalouge",row=3,column=3,\
                                   command = self.showToys)

    def showFood(self):
        self.master.destroy()
        showProducts(type="food", parent=shopCatalogue)
            
    def showMed(self):
        self.master.destroy()
        showProducts(type="medicine", parent=shopCatalogue)

    def showHygiene(self): 
        self.master.destroy()
        showProducts(type="hygiene", parent=shopCatalogue)

    def showToys(self):
        self.master.destroy()
        showProducts(type="toys", parent=shopCatalogue)


from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import *
from viewMed import View1,View2,View3,View4,View5,View6
from viewHygiene import ViewOne,ViewTwo,ViewThree,ViewFour,ViewFive,ViewSix
from viewToys import Toy1,Toy2,Toy3,Toy4,Toy5
from db import loadOrders, loadProducts, loadSession, saveOrders, loadTempOrder, saveTempOrder


products = loadProducts()
uid, cartNumber = loadSession()
cart = {}


class showProducts(EasyFrame):
    def __init__(self, type, parent=None, pagination=0):
        EasyFrame.__init__(self,title="FOOD CATALOGUE")
        self.type = type
        self.master.attributes("-fullscreen", True)
        self.setBackground("white")
        self.parent=parent
        temp = products.copy()
        temp = list(filter(lambda x: x["type"] == type, temp))

        self.nextpage=self.addButton(text="Checkout",row=8,column=0,columnspan=2, command=self.checkout)
        self.back=self.addButton(text="Back to Homepage",row=8,column=2,columnspan=1,\
                                 command = self.goback)

        if len(temp) == 0:
            self.addLabel("No products found.", 1, 0, columnspan=3, rowspan=2, sticky="NSEW")
        elif len(temp) <= 6:
            temp = temp[0: len(temp)]
        elif pagination == 0:
            temp = temp[0:6]
            self.addButton(">", row=6, column=2, command=lambda page=pagination: self.pagination(page+1))
        elif pagination*6+6 >= len(temp):
            temp = temp[pagination*6:len(temp)]
            self.addButton("<", row=6, column=0, command=lambda page=pagination: self.pagination(page-1))
        else:
            temp = temp[pagination*6:pagination*6+6]
            self.addButton("<", row=7, column=0, command=lambda page=pagination: self.pagination(page-1))
            self.addButton(">", row=7, column=2, command=lambda page=pagination: self.pagination(page+1))

        self.imgs = []
        self.img_labels = []
        i = 0
        for r in range(0, 4, 3):
            for c in range(3):
                try:
                    product = temp[i]
                except IndexError:
                    break
                imgLabel = self.addLabel("", r, c, sticky="NESW")
                self.addLabel(product["name"], r+1, c, sticky="NEWS", font=("Verdana", 20, "italic"), foreground="#57a1f8")
                img = PhotoImage(file=f"images/{product['imageId']}/200x200.png")
                imgLabel["image"] = img
                self.imgs.append(img)
                self.addButton("View Product", r+2, c, command=lambda item=product: self.addToCart(item))
                i += 1

        return
    
    def pagination(self, page):
        self.master.destroy()
        showProducts(type=self.type, pagination=page)

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()

    def addToCart(self, item):
        ViewProduct(item)
    
    def checkout(self):
        Checkout()


class ViewProduct(EasyFrame, Toplevel):
    def __init__(self, item):
        EasyFrame.__init__(self, "View Products")
        Toplevel.__init__(self)
        self.setBackground("white")

        self.img = self.addLabel("", 0, 0, columnspan=2)
        img = PhotoImage(file=f"images/{item['imageId']}/200x200.png")
        self.img["image"] = img
        self.imgs = [img]

        self.addLabel(item["name"], 1, 0, sticky="NESW", columnspan=2)
        self.addLabel("Price:", 2, 0, sticky="NES")
        self.addLabel(f"{'RM%.2f' % item['price']}", 2, 1, sticky="NEWS")
        # self.addLabel("Rating:", 3, 0, sticky="NES")
        # self.addLabel(f'{item["totalStars"] / item["sold"]} / 5')
        self.addLabel("Quantity:", 3, 0, sticky="ENS")
        quantity = cart.get(item["id"], {"quantity": 0})["quantity"]
        self.quantity = self.addIntegerField(quantity, 3, 1)

        self.addButton("Buy", 4, 0, command=lambda item=item: self.saveInCart(item), columnspan=2)

    def saveInCart(self, item):
        cart[item["id"]] = item
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
        for v in cart.values():
            text += format % (v["name"], v["price"], v["quantity"], v["price"] * v["quantity"]) + '\n'
            total += v["price"] * v["quantity"]


        self.addTextArea(text, 1, 0)
        self.addLabel(f"Price: RM{'%.2f'%total}", 2, 0)
        self.addButton("Pay", command=self.pay, row=3, column=0)

    def pay(self):
        self.messageBox("Payment Successful!", message="Thank you for ordering with us! Your order is on its way ^..^")
        self.master.destroy()

    
#MEDICINE CATALOGUE
class showMed(EasyFrame):
    def __init__(self,parent=None):
        EasyFrame.__init__(self,title="MEDICINE CATALOGUE")
        self.setSize(700,800)
        self.setBackground("white")
        self.parent=parent
        
        #image 1
        imageLabel1 = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        textLabel1 = self.addLabel(text="wound spray", row=1, column=0,\
                                   sticky="NSEW")
        self.image1 = PhotoImage(file="med1.png")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=0,\
                                  command=View1)

        #image 2
        imageLabel2 = self.addLabel(text="", row=0, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="PurrScription", row=1, column=1,\
                                   sticky="NSEW")
        self.image2 = PhotoImage(file="med2.png")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=1,\
                                  command=View2)

        #image 3
        imageLabel3 = self.addLabel(text="", row=0, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="antibiotic", row=1, column=2,\
                                   sticky="NSEW")
        self.image3 = PhotoImage(file="med3.png")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=2,\
                                  command=View3)

        #image 4
        imageLabel4 = self.addLabel(text="", row=3, column=0, sticky="NSEW")
        textLabel4 = self.addLabel(text="wormer", row=4, column=0,\
                                   sticky="NSEW")
        self.image4 = PhotoImage(file="med4.png")
        imageLabel4["image"] = self.image4
        font4 = Font(family="Verdana", size=20, slant="italic")
        textLabel4["font"] = font4
        textLabel4["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=0,\
                                  command=View4)

        #image 5
        imageLabel5 = self.addLabel(text="", row=3, column=1, sticky="NSEW")
        textLabel5 = self.addLabel(text="revolution PLUS", row=4, column=1,\
                                   sticky="NSEW")
        self.image5 = PhotoImage(file="med5.png")
        imageLabel5["image"] = self.image5
        font5 = Font(family="Verdana", size=20, slant="italic")
        textLabel5["font"] = font5
        textLabel5["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=1,\
                                  command=View5)

        #image 6
        imageLabel6 = self.addLabel(text="", row=3, column=2, sticky="NSEW")
        textLabel6 = self.addLabel(text="Flea Treatment", row=4, column=2,\
                                   sticky="NSEW")
        self.image6 = PhotoImage(file="med6.png")
        imageLabel6["image"] = self.image6
        font6 = Font(family="Verdana", size=20, slant="italic")
        textLabel6["font"] = font6
        textLabel6["foreground"] = "#57a1f8"
        self.buy= self.addButton(text="view product",row=5,column=2,\
                                 command=View6)

        self.nextpage=self.addButton(text="cart",row=6,column=0,columnspan=2)
        self.back=self.addButton(text="homepage",row=6,column=1,columnspan=2,\
                                 command=self.goback)

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()

#HYGIENE CATALOGUE
class showHygiene(EasyFrame):
    def __init__(self,parent=None):
        EasyFrame.__init__(self,title="HYGIENE CATALOGUE")
        self.setSize(700,800)
        self.setBackground("white")
        self.parent=parent
        
        #image 1
        imageLabel1 = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        textLabel1 = self.addLabel(text="brush", row=1, column=0,\
                                   sticky="NSEW")
        self.image1 = PhotoImage(file="hygiene1.png")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=0,\
                                  command=ViewOne)

        #image 2
        imageLabel2 = self.addLabel(text="", row=0, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="nail clipper", row=1, column=1,\
                                   sticky="NSEW")
        self.image2 = PhotoImage(file="hygiene2.png")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=1,\
                                  command=ViewTwo)

        #image 3
        imageLabel3 = self.addLabel(text="", row=0, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="litter box", row=1, column=2,\
                                   sticky="NSEW")
        self.image3 = PhotoImage(file="hygiene3.png")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=2,\
                                  command=ViewThree)

        #image 4
        imageLabel4 = self.addLabel(text="", row=3, column=0, sticky="NSEW")
        textLabel4 = self.addLabel(text="shampoo", row=4, column=0,\
                                   sticky="NSEW")
        self.image4 = PhotoImage(file="hygiene4.png")
        imageLabel4["image"] = self.image4
        font4 = Font(family="Verdana", size=20, slant="italic")
        textLabel4["font"] = font4
        textLabel4["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=0,\
                                  command=ViewFour)

        #image 5
        imageLabel5 = self.addLabel(text="", row=3, column=1, sticky="NSEW")
        textLabel5 = self.addLabel(text="toothbrush", row=4, column=1,\
                                   sticky="NSEW")
        self.image5 = PhotoImage(file="hygiene5.png")
        imageLabel5["image"] = self.image5
        font5 = Font(family="Verdana", size=20, slant="italic")
        textLabel5["font"] = font5
        textLabel5["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=1,\
                                  command=ViewFive)

        #image 6
        imageLabel6 = self.addLabel(text="", row=3, column=2, sticky="NSEW")
        textLabel6 = self.addLabel(text="litter scoop", row=4, column=2,\
                                   sticky="NSEW")
        self.image6 = PhotoImage(file="hygiene6.png")
        imageLabel6["image"] = self.image6
        font6 = Font(family="Verdana", size=20, slant="italic")
        textLabel6["font"] = font6
        textLabel6["foreground"] = "#57a1f8"
        self.buy= self.addButton(text="view product",row=5,column=2,\
                                 command=ViewSix)

        self.nextpage=self.addButton(text="cart",row=6,column=0,columnspan=2)
        self.back=self.addButton(text="homepage",row=6,column=1,columnspan=2,\
                                 command=self.goback)

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()

#TOYS CATALOGUE
class showToys(EasyFrame):
    def __init__(self,parent=None):
        EasyFrame.__init__(self,title="TOYS CATALOGUE")
        self.setSize(700,800)
        self.setBackground("white")
        self.parent=parent
        
        #image 1
        imageLabel1 = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        textLabel1 = self.addLabel(text="spring toy", row=1, column=0,\
                                   sticky="NSEW")
        self.image1 = PhotoImage(file="toys1.png")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=0,\
                                  command=Toy1)

        #image 2
        imageLabel2 = self.addLabel(text="", row=0, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="balls", row=1, column=1,\
                                   sticky="NSEW")
        self.image2 = PhotoImage(file="toys2.png")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=1,\
                                  command=Toy2)

        #image 3
        imageLabel3 = self.addLabel(text="", row=0, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="feather wand", row=1, column=2,\
                                   sticky="NSEW")
        self.image3 = PhotoImage(file="toys3.png")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=2,\
                                  command=Toy3)

        #image 4
        imageLabel4 = self.addLabel(text="", row=3, column=0, sticky="NSEW")
        textLabel4 = self.addLabel(text="chew toy", row=4, column=0,\
                                   sticky="NSEW")
        self.image4 = PhotoImage(file="toys4.png")
        imageLabel4["image"] = self.image4
        font4 = Font(family="Verdana", size=20, slant="italic")
        textLabel4["font"] = font4
        textLabel4["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=0,\
                                  command=Toy4)

        #image 5
        imageLabel5 = self.addLabel(text="", row=3, column=1, sticky="NSEW")
        textLabel5 = self.addLabel(text="mouse toy", row=4, column=1,\
                                   sticky="NSEW")
        self.image5 = PhotoImage(file="toys5.png")
        imageLabel5["image"] = self.image5
        font5 = Font(family="Verdana", size=20, slant="italic")
        textLabel5["font"] = font5
        textLabel5["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=1,\
                                  command=Toy5)


        self.back=self.addButton(text="homepage",row=6,column=1,columnspan=2,\
                                 command=self.goback)

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()






        
def main():
    shopCatalogue().mainloop()

if __name__=="__main__":
    main()
        

        
