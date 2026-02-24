inventory = {
    "Bread": [30, 50, 10, False],
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    print(f"Processing {item}")
    
    current_stock, min_stock, restock_qty, on_sale = inventory[item]
    
    # Nachfüllen mit while-Schleife
    while current_stock < min_stock:
        current_stock += restock_qty
    
    # Rabatt prüfen
    if current_stock > discount_threshold and not on_sale:
        on_sale = True
    
    # Werte zurück ins Dictionary speichern
    inventory[item] = [current_stock, min_stock, restock_qty, on_sale]

print("Processing completed")