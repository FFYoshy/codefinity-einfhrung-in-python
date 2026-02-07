# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

# R1 Kein Rabatt, "Non-Perishable" 
# R2 10 % Rabatt, 7 Tagen oder mehr abläuft, oder der Lagerbestand 50 Einheiten oder weniger beträgt;
# R3 20 % Rabatt, wenn das Produkt in 4 bis 6 Tagen abläuft und der Lagerbestand über50 Einheiten liegt;
# R4 30 % Rabatt, wenn das Produkt in 3 Tagen oder weniger abläuft und der Lagerbestand über50 Einheiten liegt;

if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        print ("30% discount applied")
    elif days_until_expiration >= 4 and days_until_expiration <= 6 and stock_level > 50:
        print ("20% discount applied")
    elif days_until_expiration > 6 and stock_level <= 50:
        print ("10% discount applied")
else:
    print ("No discount available for non-perishable items.")
