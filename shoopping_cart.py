#add to cart feature which automatically calc the amount 
def displayCart(cart):
    if not cart:
        print("Your cart is empty! Please add something to the cart.")
    else:
        print("My cart: ")
    
    total = 0
    for item in cart:
        print(f"{item['name']}: ${item['price']:.2f}")
        total += item['price']
    print(f"Total: ${total:.2f}")

def main():
    cart = []
    while True:
        print("\nMy Cart")
        print("\n1. Add product to cart")
        print("\n2. View Cart")
        print("\n3. Remove item from the cart")
        print("\n4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter the product name: ")
            price = float(input("Enter the price: $"))
            product = {"name": name, "price": price}
            cart.append(product)
            print("Product added to cart!")
        
        elif choice == '2':
            displayCart(cart)
        
        elif choice == '3':
            if not cart:
                print("Oh no! Your cart is empty. No products to be removed.")
            else:
                displayCart(cart)
                itemIndex = int(input("Enter the product number to remove: ")) - 1
                if 0 <= itemIndex < len(cart):
                    removeItem = cart.pop(itemIndex)
                    print(f"Removed item: {removeItem['name']}")
                else:
                    print("Invalid product number. Failed to remove")  
        elif choice == '4':
            print("Exiting...") 
            break
        else: 
            print("Invalid choice. Please select a valid option")

if __name__ == "__main__":
    main()
