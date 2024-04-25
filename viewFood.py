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

class ViewWhiskas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="food1.png")
        image_label["image"] = image

        Label(self, text="Whiskas wetfood\nGreat Food for your pet!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM20.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class ViewSmart(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="food2.png")
        image_label["image"] = image

        Label(self, text="Smart Heart wetfood\nYour pet would LOVE it!").grid(row=1, column=0, sticky="s", rowspan=2)
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

class ViewPro(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="food3.png")
        image_label["image"] = image

        Label(self, text="ProDiet wetfood\nyour pet gonna be fit!").grid(row=1, column=0, sticky="s", rowspan=2)
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

class ViewSnappy(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="food4.png")
        image_label["image"] = image

        Label(self, text="SnappyTom dryfood\ndon't let tom be snappy!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM35.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class ViewHills(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="food5.png")
        image_label["image"] = image

        Label(self, text="Hills dryfood\nsuper yummy!Favourite!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM30.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class ViewIAMSO(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="food6.png")
        image_label["image"] = image

        Label(self, text="IAOMSO dryfood\nall time favourite, no miss!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM30.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

        


