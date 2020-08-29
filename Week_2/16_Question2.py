"""
You own a Dunkin Donut store that sells doughnuts for $1.29.
A customer stops by to buy as much as doughnuts possible for $10.
Write a program to calculate how many doughnuts the customer can buy.
The customer will not be satisfied if you sell partial doughnuts.
"""
donut_price = 1.29
customer_money = 10

total = int(customer_money // donut_price)
print(total, "donuts can be bought")

