from tkinter import *

base = Tk()
base.geometry("400x150")

def receipt():
    top = Toplevel()
    top.geometry("400x150")
    top.config(background="sky blue")

    with open('db/orders.txt', 'r') as file:
        total_cost = 0  # calculate the total cost
        for line in file:
            id__, imageID, company, name, price, unit, sold = line.strip().split(",")
            price = float(price)  
            unit = int(unit)  
            total = price * unit
            total_cost += total  #add the total cost
            tax = 0.1*total_cost
            overall_cost = tax + total_cost

            # display each item on the receipt
            item_label = Label(top, text=f'{company}\t{name}\t{price}\t{unit}\t{total}')
            item_label.pack()
            item_label.config(background="white")

    #display total cost
    totalLabel = Label(top, text=f'Total cost: {overall_cost}')
    totalLabel.pack()
    totalLabel.config(background="sky blue")

    
    headerLabel = Label(top, text="---- PAWSOME PURCHASE RECEIPT ----")
    headerLabel.pack()
    headerLabel.config(background="sky blue")

   
    headingLabel = Label(top, text="COMPANY\tNAME\tPRICE\tUNIT\tTOTAL")
    headingLabel.pack()
    headingLabel.config(background="white")

b = Button(base, text="Print receipt", command=receipt)
b.pack(padx=10, pady=10)

base.mainloop()
