# Request price from user
price = input("Enter the price of a meal: ")

# Calculate tip and total
tip = float(price) * 0.16
total = float(price) + tip

# Return tip and total to user
print("A 16% tip would be", "{:.2f}".format(tip))
print("The total including tip would be", '{:.2f}'.format(total))
