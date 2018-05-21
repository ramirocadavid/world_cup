# Request gallons and convert to equivalent units
gallons = float(input("Enter number of gallons of gasoline: "))
liters = gallons * 3.7854
barrels = gallons / 19.5
price = gallons * 3.65

# Print gallons and equivalent units
print(gallons, "gallons of gasoline is equivalent to", "{:.4f}".format(liters), "liters, which require", \
      "{:.3f}".format(barrels), "barrels to be produced, and its price is", "${:.2f}".format(price), "U.S. dollars")
