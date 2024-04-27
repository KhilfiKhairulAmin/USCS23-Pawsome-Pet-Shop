from tkinter import *

base = Tk()
base.geometry("400x150")

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

b = Button(base, text="Print receipt", command=receipt)
b.pack(padx=10, pady=10)


base.mainloop()
