prices = [100, 200, 300]
discount = 10 #10% discount
final_prices = []

for price in prices:
    final_price = price -(price * discount/100)
    final_prices.append(final_price)
print(final_prices)

# -> for big data it is complex for using loops

