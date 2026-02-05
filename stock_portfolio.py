import json
import os

class StockPortfolio:
    def __init__(self, filename="portfolio.json"):
        self.filename = filename
        self.portfolio = self.load_portfolio()
        # Mock stock prices for demonstration
        self.market_prices = {
            "AAPL": 180.50,
            "TSLA": 250.25,
            "GOOGL": 145.10,
            "AMZN": 170.00,
            "MSFT": 405.30
        }

    def load_portfolio(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save_portfolio(self):
        with open(self.filename, 'w') as f:
            json.dump(self.portfolio, f, indent=4)

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        self.save_portfolio()
        print(f"Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol, shares):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= shares:
                self.portfolio[symbol] -= shares
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
                self.save_portfolio()
                print(f"Removed {shares} shares of {symbol}.")
            else:
                print(f"Not enough shares to remove. Current balance: {self.portfolio[symbol]}")
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def display_portfolio(self):
        print("\n--- Current Stock Portfolio ---")
        total_value = 0
        print(f"{'Symbol':<10} | {'Shares':<10} | {'Price':<10} | {'Value':<10}")
        print("-" * 45)
        
        for symbol, shares in self.portfolio.items():
            price = self.market_prices.get(symbol, 0)
            value = shares * price
            total_value += value
            print(f"{symbol:<10} | {shares:<10} | ${price:<9.2f} | ${value:<9.2f}")
        
        print("-" * 45)
        print(f"{'TOTAL PORTFOLIO VALUE: ':<32} ${total_value:<9.2f}\n")

def main():
    tracker = StockPortfolio()
    
    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ")
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares to remove: "))
            tracker.remove_stock(symbol, shares)
        elif choice == '3':
            tracker.display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
