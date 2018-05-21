# Request input from user
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
numType = int(input("Enter an average type (1 for Arithmetic, 2 for geometric, and 3 for root-mean-square): "))

# Calculate and output average based on type selected by user
if numType == 1:
    avg = (a + b) / 2
    type = "arithmetic mean"
elif numType == 2:
    avg = (a * b) ** 0.5
    type = "geometric mean"
else:
    avg = ((a**2 + b**2)/2) ** 0.5
    type = "root-mean-square"
print("The", type, "of", a, "and", b, "is", avg, "(rounded to 4 decimals, it is\
 equal to", '{:.4f}'.format(avg), ")")
