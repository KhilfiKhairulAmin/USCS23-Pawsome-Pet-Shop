from tkinter import *
from db import loadProducts, loadOrders, saveOrders

class ShoppingCart:
    def __init__(self, master=None):
        self.items = {}

        self.addButton(text="Add item to cart", row =1, column = 0, command=self.addItem)

        self.removeButton(text="Remove item from cart", row = 2, column = 0, command=self.removeItem)

        self.displayButton(text="Your cart", row = 3, column = 0, command=self.displayCart)

        self.receiptButton(text="Your receipt", row = 4, column = 0, command=self.receipt)
        

    def addItem(self, id, quantity=1):  
        with open("products.txt", 'r') as file:
            next(file)
            for line in file:
                id_, imageId, company, name, price, unit, sold = line.strip().split(',')
                if id_ not in self.items:
                # If ID does not exist in cart, add it
                    self.items[id_] = {
                        "name": name,
                        "price": float(price),
                        "quantity": quantity
                }
                else:
                # If ID already exists in cart, update its quantity
                    self.items[id_]['quantity'] += quantity


    def calculateTotal(self): 
        total = sum(item["price"] * item["quantity"] for item in self.items.values())
        return total

    def displayCart(self):  
        print("Your cart:")
        for id, item_info in self.items.items():
            print(f"Item ID: {id}, Name: {item_info['name']}, Price: ${item_info['price']}, Quantity: {item_info['quantity']}")
        print(f"Total items: {sum(item['quantity'] for item in self.items.values())}")
        print(f"Total price: ${self.calculateTotal()}")

    def removeItem(self):
        id = "1"  # Example ID, replace it with your logic to get the item ID
        quantity = 1  # Example quantity, you can modify this as needed
        if id in self.items:
            if self.items[id]['quantity'] <= quantity:
                del self.items[id]
            else:
                self.items[id]['quantity'] -= quantity
        else:
            print("Item not found in cart.")

    def receipt(self): 
        top = Toplevel()
        top.geometry("400x150")
        top.config(background="sky blue")

        total_cost = self.calculateTotal()  
        tax = 0.1 * total_cost
        overall_cost = tax + total_cost

        for id, item_info in self.items.items():
            item_label = Label(top, text=f'{id} - {item_info["name"]} - ${item_info["price"]} - Quantity: {item_info["quantity"]}')
            item_label.pack()
            item_label.config(background="white")

        totalLabel = Label(top, text=f'Total cost: {overall_cost}')
        totalLabel.pack()
        totalLabel.config(background="sky blue")

        headerLabel = Label(top, text="---- PURCHASE RECEIPT ----")
        headerLabel.pack()
        headerLabel.config(background="sky blue")

        headingLabel = Label(top, text="ID - NAME - PRICE - QUANTITY")
        headingLabel.pack()
        headingLabel.config(background="white")

def main():
    productFile = "products.txt"
    products = loadProducts()
    orders = loadOrders()
    cart = ShoppingCart()

    saveOrders(orders)

if __name__ == "__main__":
    main()
