# Request income
income = int(input("Please enter your income: "))

# Calculate tax owed
if income <= 1000:
    tax = income * 0.05
elif income <= 2000:
    tax = (1000 * 0.05) + ((income - 1000) * 0.1)
else:
    tax = (1000 * 0.05) + (1000 * 0.1) + ((income - 2000) * 0.15)

# Return tax owed
print("The tax owed is:", "${:.0f}".format(tax))
