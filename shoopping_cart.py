from tkinter import *

class shoppingCart:
    def __init__(self):
        self.items = {}

    def addItem(self, id, quantity=1): #kena add button 
        with open("products.txt", 'r') as file:
            next(file)
            for line in file:
                id_, imageId, company, name, price, unit, sold = line.strip().split(',')
                self.items[id_] = {
                    "name": name,
                    "price": float(price),
                    "quantity": quantity
                }

    def calculateTotal(self): 
        total = sum(item["price"] * item["quantity"] for item in self.items.values())
        return total

    def displayCart(self): # kena add button 
        print("Your cart:")
        for id, item_info in self.items.items():
            print(f"Item ID: {id}, Name: {item_info['name']}, Price: ${item_info['price']}, Quantity: {item_info['quantity']}")
        print(f"Total items: {sum(item['quantity'] for item in self.items.values())}")
        print(f"Total price: ${self.calculateTotal()}")

    def removeItem(self, id, quantity=1): #kena add button 
        if id in self.items:
            if self.items[id]['quantity'] <= quantity:
                del self.items[id]
            else:
                self.items[id]['quantity'] -= quantity
        else:
            print("Item not found in cart.")

    def receipt(self): #kena add button 
        top = Toplevel()
        top.geometry("400x150")
        top.config(background="sky blue")

        total_cost = self.calculateTotal()  # calculate the total cost
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

#payment method - radio button 

def main():
    productFile = "products.txt"
    cart = shoppingCart()

    cart.addItem("1", 2)  #example of adding item with ID "1" and quantity 2
    cart.displayCart()
    cart.removeItem("1")  #example of removing item with ID "1"
    cart.displayCart()
    cart.receipt()



if __name__ == "__main__":
    main()
