from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import *

class InputIntegerField(Entry):
    def __init__(self, master=None, width=10, **kwargs):
        self.var = StringVar()
        super().__init__(master, textvariable=self.var,\
                         width=width,**kwargs)

        self.var.trace_add("write", self.validate_input)

    def validate_input(self, *args):
        value = self.var.get()
        if not value.isdigit():
            self.var.set("0")
            
class ViewOne(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="hygiene1.png")
        image_label["image"] = image

        Label(self, text="cat fur brush\nbrush for your pretty pet").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM10.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class ViewTwo(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="hygiene2.png")
        image_label["image"] = image

        Label(self, text="nail clipper\nso your cat don't hurt you!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM5.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class ViewThree(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="hygiene3.png")
        image_label["image"] = image

        Label(self, text="litter box\ntoilet made for your cat").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM25.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class ViewFour(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="hygiene4.png")
        image_label["image"] = image

        Label(self, text="cat shampoo\nfor a nice smelling cat!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM15.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

        
class ViewFive(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="hygiene5.png")
        image_label["image"] = image

        Label(self, text="toothbrush\nfor nice looking teeth!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM11.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

        
class ViewSix(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="hygiene6.png")
        image_label["image"] = image

        Label(self, text="litter scoop\nlitter box without scoop?\nNO!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM10.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()
