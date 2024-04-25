from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import *
from showProducts import showFood,showMed,showHygiene,showToys

class shopCatalogue (EasyFrame):
    def __init__(self, userId):
        self.userId = userId
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
        self.image1 = PhotoImage(file="")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"

        #image 2
        imageLabel2 = self.addLabel(text="", row=1, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="MEDICINE", row=2, column=1,\
                                   sticky="NSEW")
        self.image2 = PhotoImage(file="")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"

        #image 3
        imageLabel3 = self.addLabel(text="", row=1, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="HYGIENE", row=2, column=2,\
                                   sticky="NSEW")
        self.image3 = PhotoImage(file="")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"

        #image 4
        imageLabel4 = self.addLabel(text="", row=1, column=3, sticky="NSEW")
        textLabel4 = self.addLabel(text="TOYS", row=2, column=3,\
                                   sticky="NSEW")
        self.image4 = PhotoImage(file="")
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
        showFood(shopCatalogue)

            
    def showMed(self):
        self.master.destroy()
        showMed(shopCatalogue)

    def showHygiene(self): 
        self.master.destroy()
        showHygiene(shopCatalogue)

    def showToys(self):
        self.master.destroy()
        showToys(shopCatalogue)
        

        
def main():
    shopCatalogue().mainloop()

if __name__=="__main__":
    main()
        

        
