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


class View1(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="med1.png")
        image_label["image"] = image

        Label(self, text="Wound Spray\ndon't let your pet hurt").grid(row=1, column=0, sticky="s", rowspan=2)
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

class View2(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="med2.png")
        image_label["image"] = image

        Label(self, text="PurrScription PLUS\nkill all the enemies!").grid(row=1, column=0, sticky="s", rowspan=2)
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

class View3(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="med3.png")
        image_label["image"] = image

        Label(self, text="NATURAL antibiotic\nhealthy pet,happy pet").grid(row=1, column=0, sticky="s", rowspan=2)
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

class View4(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="med4.png")
        image_label["image"] = image

        Label(self, text="WORMER\ntapeworm?? no more!").grid(row=1, column=0, sticky="s", rowspan=2)
        Label(self, text="Price:").grid(row=1, column=1, sticky="nsew")
        Label(self, text="RM18.00").grid(row=2, column=1, sticky="nsew")

        quantity_label = Label(self, text="Quantity:")
        quantity_label.grid(row=3, column=0)
        
        self.quantity_entry = InputIntegerField(self,width=3)
        self.quantity_entry.grid(row=3, column=1)
        
        Button(self, text="Buy").grid(row=4, column=0)
        Button(self, text="Back",command=self.goback).grid(row=4, column=1)

    def goback(self):
        self.destroy()

class View5(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="med5.png")
        image_label["image"] = image

        Label(self, text="revolution PLUS\ninsects? no pleaseeee").grid(row=1, column=0, sticky="s", rowspan=2)
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

class View6(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("VIEW PRODUCTS")
        self.geometry("300x300")

        image_label = Label(self, text="", bg="white")
        image_label.grid(row=0, column=0, columnspan=2)

        image = PhotoImage(file="med6.png")
        image_label["image"] = image

        Label(self, text="Flea Treatment\nno fleas anymore yeay!").grid(row=1, column=0, sticky="s", rowspan=2)
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
