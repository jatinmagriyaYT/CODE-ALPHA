def stock_portfolio_tracker():
    # Hardcoded stock prices (in USD)
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "MSFT": 300.20,
        "AMZN": 120.90,
        "GOOGL": 135.60
    }
    
    print("Welcome to Simple Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    portfolio = {}
    total_value = 0.0
    
    while True:
        print("\n1. Add stock to portfolio")
        print("2. View current portfolio")
        print("3. Calculate total investment")
        print("4. Save portfolio to file")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            stock_name = input("Enter stock symbol: ").upper()
            if stock_name not in stock_prices:
                print(f"Error: {stock_name} is not in our price database.")
                continue
                
            try:
                quantity = int(input(f"Enter quantity of {stock_name}: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                    
                portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
                print(f"Added {quantity} shares of {stock_name} to portfolio.")
                
            except ValueError:
                print("Please enter a valid integer for quantity.")
                
        elif choice == "2":
            if not portfolio:
                print("Your portfolio is empty.")
            else:
                print("\nCurrent Portfolio:")
                for stock, qty in portfolio.items():
                    print(f"{stock}: {qty} shares")
                    
        elif choice == "3":
            total_value = sum(portfolio.get(stock, 0) * stock_prices[stock] 
                            for stock in portfolio)
            print(f"\nTotal Portfolio Value: ${total_value:.2f}")
            
        elif choice == "4":
            if not portfolio:
                print("Cannot save empty portfolio.")
                continue
                
            filename = input("Enter filename to save (e.g., portfolio.txt): ")
            try:
                with open(filename, 'w') as f:
                    f.write("Stock Portfolio Summary\n")
                    f.write("======================\n")
                    for stock, qty in portfolio.items():
                        value = qty * stock_prices[stock]
                        f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]:.2f} = ${value:.2f}\n")
                    f.write(f"\nTotal Value: ${total_value:.2f}")
                print(f"Portfolio saved to {filename}")
            except:
                print("Error saving file.")
                
        elif choice == "5":
            print("Exiting portfolio tracker. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-5.")

# Start the portfolio tracker
stock_portfolio_tracker()