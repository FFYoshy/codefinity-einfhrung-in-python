inventory = {
    "Bread": [42, 1.20, 0.99],
    "Eggs": [225, 2.12, 1.99],
    "Apples": [9, 1.50, 1.35]
}

for item in inventory:
    stock, regular_price, discounted_price = inventory[item]

    if stock < 30:
        print(f"{item} need restocking.")
    elif stock > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    else:
        print(f"{item} should be sold at the regular price of {regular_price}.")