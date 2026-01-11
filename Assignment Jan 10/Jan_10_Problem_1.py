# Problem 1: The "Price Tagger"
# The Challenge: You are given a list of product prices. You need to write a function that takes this list and a "Discount Percentage." Inside the function, use a list comprehension to create a new list where each price is reduced by that percentage.

# prices = [100, 250, 400, 50]

prices = [100, 250, 400, 50]
def apply_discount(prices, discount_percent=10):
    return [price * (1 - discount_percent / 100) for price in prices]

disPrices = apply_discount(prices)
print(disPrices)  
# d = 10
# disPrices = []
# def par():
#     for i in prices:
#         disPrices.append(i*.9)

#     return disPrices
# par()
# print(disPrices)