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

class Toy1(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="toys1.png")
        image_label["image"] = image

        Label(self, text="spring toy\nwhats more fun than SPRING?!").grid(row=1, column=0, sticky="s", rowspan=2)
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

        
class Toy2(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="toys2.png")
        image_label["image"] = image

        Label(self, text="balls\ncolourful balls? I'm on!").grid(row=1, column=0, sticky="s", rowspan=2)
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

class Toy3(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="toys3.png")
        image_label["image"] = image

        Label(self, text="feather wand\nfun to catch around!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM7.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class Toy4(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="toys4.png")
        image_label["image"] = image

        Label(self, text="chew toy\nmmmm!nice chewing toys!").grid(row=1, column=0, sticky="s", rowspan=2)
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

class Toy5(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="toys5.png")
        image_label["image"] = image

        Label(self, text="mouse toy\nfor your pet to chase!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM17.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

