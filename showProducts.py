from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import *
from viewFood import ViewWhiskas,ViewSmart,ViewPro,ViewSnappy,ViewHills,ViewIAMSO
from viewMed import View1,View2,View3,View4,View5,View6
from viewHygiene import ViewOne,ViewTwo,ViewThree,ViewFour,ViewFive,ViewSix
from viewToys import Toy1,Toy2,Toy3,Toy4,Toy5

class showFood(EasyFrame):
    def __init__(self,parent=None):
        EasyFrame.__init__(self,title="FOOD CATALOGUE")
        self.master.attributes("-fullscreen", True)
        self.setBackground("white")
        self.parent=parent
        
        #image 1
        imageLabel1 = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        textLabel1 = self.addLabel(text="Whiskas wetfood", row=1, column=0,\
                                   sticky="NSEW")
        self.image1 = PhotoImage(file="food1.png")
        imageLabel1["image"] = self.image1
        font1 = Font(family="Verdana", size=20, slant="italic")
        textLabel1["font"] = font1
        textLabel1["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=0,\
                                  command=ViewWhiskas)

        #image 2
        imageLabel2 = self.addLabel(text="", row=0, column=1, sticky="NSEW")
        textLabel2 = self.addLabel(text="Smart Heart wetfood", row=1, column=1,\
                                   sticky="NSEW")
        self.image2 = PhotoImage(file="food2.png")
        imageLabel2["image"] = self.image2
        font2 = Font(family="Verdana", size=20, slant="italic")
        textLabel2["font"] = font2
        textLabel2["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=1,\
                                  command=ViewSmart)

        #image 3
        imageLabel3 = self.addLabel(text="", row=0, column=2, sticky="NSEW")
        textLabel3 = self.addLabel(text="ProDiet wetfood", row=1, column=2,\
                                   sticky="NSEW")
        self.image3 = PhotoImage(file="food3.png")
        imageLabel3["image"] = self.image3
        font3 = Font(family="Verdana", size=20, slant="italic")
        textLabel3["font"] = font3
        textLabel3["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=2,column=2,\
                                  command=ViewPro)

        #image 4
        imageLabel4 = self.addLabel(text="", row=3, column=0, sticky="NSEW")
        textLabel4 = self.addLabel(text="SnappyTom dryfood", row=4, column=0,\
                                   sticky="NSEW")
        self.image4 = PhotoImage(file="food4.png")
        imageLabel4["image"] = self.image4
        font4 = Font(family="Verdana", size=20, slant="italic")
        textLabel4["font"] = font4
        textLabel4["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=0,\
                                  command=ViewSnappy)

        #image 5
        imageLabel5 = self.addLabel(text="", row=3, column=1, sticky="NSEW")
        textLabel5 = self.addLabel(text="Hills dryfood", row=4, column=1,\
                                   sticky="NSEW")
        self.image5 = PhotoImage(file="food5.png")
        imageLabel5["image"] = self.image5
        font5 = Font(family="Verdana", size=20, slant="italic")
        textLabel5["font"] = font5
        textLabel5["foreground"] = "#57a1f8"
        self.buy = self.addButton(text="view product",row=5,column=1,\
                                  command=ViewHills)

        #image 6
        imageLabel6 = self.addLabel(text="", row=3, column=2, sticky="NSEW")
        textLabel6 = self.addLabel(text="IAMSO dryfood", row=4, column=2,\
                                   sticky="NSEW")
        self.image6 = PhotoImage(file="food6.png")
        imageLabel6["image"] = self.image6
        font6 = Font(family="Verdana", size=20, slant="italic")
        textLabel6["font"] = font6
        textLabel6["foreground"] = "#57a1f8"
        self.buy= self.addButton(text="view product",row=5,column=2,\
                                 command=ViewIAMSO)

        self.nextpage=self.addButton(text="cart",row=6,column=0,columnspan=2)
        self.back=self.addButton(text="homepage",row=6,column=1,columnspan=2,\
                                 command = self.goback)

    def goback(self):
        self.master.destroy()
        self.parent().mainloop()
        



    
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





