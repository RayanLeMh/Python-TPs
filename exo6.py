price = float(input("Please type in a price:"))
print("Dinars:", int(price))
price = (price - int(price))*100
print("Centimes:", int(price)+1)