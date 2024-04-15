menu = ["pie", "coffee", "tea", "panini", "cookies"]
stock = {'pie': 7, 'coffee': 12, 'tea': 14, 'panini': 23, 'cookies': 32}
price = {'pie': 3.25, 'coffee': 2.43, 'tea': 1.99, 'panini': 5.47, 'cookies': 1.49}

total_stock = 0
print(stock['pie'])
for item in stock:
    total_stock = total_stock + (stock[item] * price[item])
print(f"Total stock worth is: £{total_stock}")
