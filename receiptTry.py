from tkinter import *
from starRating import StarRating  # Import your StarRating class from the starRating module

def receipt():
    top = Toplevel()
    top.geometry("400x400")
    top.config(background="sky blue")

    # Display receipt header
    header_label = Label(top, text="--- PAWSOME PURCHASE RECEIPT ---", bg="sky blue")
    header_label.pack(side=TOP)

    orders = [
        {"company": "Whiskas", "name": "Dry Food", "price": 10.0, "unit": 2, "total": 20.0},
        {"company": "Royal Canin", "name": "Dry Food", "price": 15.0, "unit": 3, "total": 45.0},
        {"company": "Snappy Tom", "name": "Wet Food", "price": 20.0, "unit": 1, "total": 20.0}
    ]

    total_cost = 0

    # Create a frame to display the receipt in a table-like format
    receipt_frame = Frame(top, bg="sky blue")
    receipt_frame.pack(fill=BOTH, expand=True)

    # Display table headers
    headers = ["COMPANY", "NAME", "PRICE", "UNIT", "TOTAL"]
    for i, header in enumerate(headers):
        header_label = Label(receipt_frame, text=header, bg="sky blue")
        header_label.grid(row=0, column=i, padx=5, pady=5)

    # Display each product in a row
    for idx, order in enumerate(orders):
        company = order['company']
        name = order['name']
        price = float(order['price'])
        unit = int(order['unit'])
        total = price * unit
        total_cost += total

        # Display product details in corresponding columns
        product_details = [company, name, f"${price:.2f}", unit, f"${total:.2f}"]
        for col, detail in enumerate(product_details):
            detail_label = Label(receipt_frame, text=detail, bg="sky blue")
            detail_label.grid(row=idx + 1, column=col, padx=5, pady=5)

    tax = 0.1 * total_cost
    overall_cost = tax + total_cost

    # Display total cost
    total_label = Label(top, text=f"Total cost: ${(overall_cost - tax):.2f}\n10 % tax: ${tax:.2f}\nOverall cost = ${overall_cost}\nThank you for purchasing with us!", bg="sky blue")
    total_label.pack()

    # Button to open the star rating window
    rating_button = Button(top, text="Give Rating", command=lambda: open_rating_window(top))
    rating_button.pack(pady=10)

def open_rating_window(parent):
    rating_window = Toplevel()
    rating_window.title("Give Rating")

    # Create and pack the StarRating widget in the rating window
    rating_frame = StarRating(rating_window, numStars=5, callback=lambda rating: on_rating_submit(rating, parent))
    rating_frame.pack(pady=20)

def on_rating_submit(rating, parent):
    print("You rated:", rating)
    # Optionally, you can save the rating to a file or perform other actions here

    # Close the parent window (receipt window)
    parent.destroy()

if __name__ == "__main__":
    base = Tk()
    base.geometry("400x150")
    base.title("Purchase Receipt and Rating")

    # Button to print the receipt
    print_receipt_button = Button(base, text="Print Receipt", command=receipt)
    print_receipt_button.pack(padx=10, pady=10)

    base.mainloop()
