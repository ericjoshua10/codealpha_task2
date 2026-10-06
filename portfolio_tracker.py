"""
CodeAlpha — Task 2: Stock Portfolio Tracker
Hardcoded prices, user enters name + quantity, total is printed and saved.
Key concepts: dictionary, input/output, arithmetic, file handling.
"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 175,
}


def show_menu():
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")


def collect_holdings():
    holdings = {}
    print("Enter stock symbol and quantity. Type 'done' when finished.")
    while True:
        symbol = input("Symbol (or done): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown symbol. Pick one from the list.")
            continue
        raw_qty = input(f"Quantity of {symbol}: ").strip()
        if not raw_qty.isdigit() or int(raw_qty) <= 0:
            print("Quantity must be a positive whole number.")
            continue
        qty = int(raw_qty)
        holdings[symbol] = holdings.get(symbol, 0) + qty
    return holdings


def build_report(holdings):
    lines = ["Stock Portfolio Report", "-" * 32]
    total = 0
    for symbol, qty in holdings.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        lines.append(f"{symbol}: {qty} x ${price} = ${value}")
    lines.append("-" * 32)
    lines.append(f"Total investment: ${total}")
    return "\n".join(lines), total


def save_report(text):
    choice = input("Save report? (txt/csv/no): ").strip().lower()
    if choice == "txt":
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write(text + "\n")
        print("Saved portfolio.txt")
    elif choice == "csv":
        with open("portfolio.csv", "w", encoding="utf-8") as file:
            file.write("symbol,quantity,price,value\n")
            for line in text.splitlines():
                if " x $" in line and "=" in line:
                    symbol = line.split(":")[0]
                    qty = line.split(":")[1].split("x")[0].strip()
                    price = line.split("$")[1].split(" ")[0]
                    value = line.split("$")[-1]
                    file.write(f"{symbol},{qty},{price},{value}\n")
        print("Saved portfolio.csv")
    else:
        print("Not saved.")


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    show_menu()
    holdings = collect_holdings()
    if not holdings:
        print("No stocks added.")
        return
    report, _ = build_report(holdings)
    print("\n" + report)
    save_report(report)


if __name__ == "__main__":
    main()
