products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# Verkäufe abziehen
for i in range(len(products)):
    products[i][1] -= units_sold[i][1]

# Lieferungen hinzufügen
for i in range(len(products)):
    products[i][1] += shipment_received[i][1]

print(f"Final stock levels for all products: {products}")