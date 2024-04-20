def saveStock(stocks):
    file = open("products.txt", 'w')
    file.write("id,name,price,unit,sold\n")
    for stock in stocks:
        file.write("{},{},{},{},{}\n".format(stock["company"], stock["product"], stock["price"], stock["unit"], stock["sold"]))
    file.close()


def loadStock():
    file = open('products.txt', 'r')
    next(file)  # Skip data header
    stocks = []
    for line in file:
        company, product, price, unit, sold = line.strip().split(",")
        stocks.append({
            "company": company,
            "product": product,
            "price": float(price),
            "unit": int(unit),
            "sold": int(sold)
        })
    file.close()
    return stocks


if __name__ == "__main__":
    print("TEST 1")
    overallStocks = loadStock()
    for stock in overallStocks:
        print(stock)
    print("TEST 2 (Refer products.txt for output)")
    saveStock(overallStocks)
