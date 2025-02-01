order_total = float(input("Enter the order total: "))

if order_total < 50:
    shipping_cost = 5
else:
    shipping_cost = 0

total_cost = order_total + shipping_cost
print(f"The total cost, including shipping, is: ${total_cost:.2f}")
