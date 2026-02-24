produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# Beide Listen als Elemente in groceries speichern
groceries = [produce, dairy]

# Verschachtelte Schleifen
for section in groceries:        # äußere Schleife
    for item in section:         # innere Schleife
        print(f"Item name: {item}")