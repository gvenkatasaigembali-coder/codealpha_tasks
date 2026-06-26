stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200,
    "MSFT": 300
}

total = 0

print("Stock Portfolio Tracker")
print("Available Stocks:")
for stock in stocks:
    print(stock, "-", "$", stocks[stock])

while True:
    name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if name == "DONE":
        break

    if name in stocks:
        quantity = int(input("Enter quantity: "))
        amount = stocks[name] * quantity
        total += amount
        print("Investment for", name, "=", "$", amount)
    else:
        print("Stock not available.")

print("\nTotal Investment Value = $", total)

file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total))
file.close()

print("Result saved in portfolio.txt")