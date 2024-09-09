import pandas as pd
from src.scrape_stock import price

df = pd.read_csv('stock_data.csv')

apple_data = df[df['Company'] == 'AAPL']

last_price = apple_data['Price'].iloc[-1] if not apple_data.empty else None

if last_price:
    price_diff = price - last_price
    percentage_change = (price_diff / last_price) * 100

    price_diff = round(price_diff, 2)
    percentage_change = round(percentage_change, 2)

    print(f'Price difference: ${price_diff}')
    print(f'Percentage change: {percentage_change}%')
else:
    print('No previous price found.')
