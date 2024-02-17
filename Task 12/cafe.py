menu =["cake", "salad", "soup", "cocktail", "coffee"]

# The stock value of each item is in the menu.
stock_menu = [ 5, 6, 12, 4, 2]

'''\u00a3 is from hexadecimal escape sequence. 
The print command apparently attempts to encode the string you gave to it into the 8-bit ASCII character set, 
and fails because the £ (pound sign) is not part of that set (while the dollar sign $ is).
'''
# Prices for each item are in the menu.
price_menu = ["\u00a33.5", "\u00a32.5", "\u00a34", "\u00a35", "\u00a31.75"]

# Total stock worth in the cafe.
total_stock = 0

# Use dictionary comprehension for creating new dictionaries.
stock = {menu[i]:stock_menu[i] for i in range(len(menu))}
price = {menu[i]:float(price_menu[i] .replace("\u00a3","")) for i in range(len(menu))}

for item in menu:
    # Calculation of each item value.
    item_value = stock[item] * price[item]

    # Calculation of total items/stock value in the cafe: adding each item value one by one.
    total_stock += item_value

print(f"Total stock worth in the cafe: \u00a3{total_stock}.")