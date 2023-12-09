def calculate_profit_loss(stock_info, stock_prices, current_day):
    realized_profit_loss = 0
    unrealized_profit_loss = 0

    for i, stock in enumerate(stock_info):
        quantity, purchase_day, sell_day = stock

        if sell_day == 0:
            # Stock not sold yet, calculate unrealized profit/loss
            unrealized_profit_loss += (stock_prices[i][current_day - 1] - stock_prices[i][purchase_day - 1]) * quantity
        elif current_day >= sell_day:
            # Stock sold, calculate realized profit/loss
            realized_profit_loss += (stock_prices[i][sell_day - 1] - stock_prices[i][purchase_day - 1]) * quantity

    return realized_profit_loss, unrealized_profit_loss

# Example input
N = int(input("Enter the number of stocks: "))

stock_info = []

for _ in range(N):
    stock_info.append(tuple(map(int, input().split())))

M = int(input("Enter the number of days: "))

stock_prices = [list(map(int, input().split())) for _ in range(N)]

current_day = int(input("Enter the current day: "))

# Calculate profit/loss
realized, unrealized = calculate_profit_loss(stock_info, stock_prices, current_day)

# Print the results
print("Realized Profit/Loss:", realized)
print("Unrealized Profit/Loss:", unrealized)
