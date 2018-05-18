# Enter input for calculator
first = input("Enter the first number: ")
operator = input("Enter operator: ")
second = input("Enter the second number: ")

# Return error if the input is different than +, -, * or /
if(operator == '+'):
    result = float(first) + float(second)
    print(first, operator, second, "=", result)
elif(operator == '-'):
    result = float(first) - float(second)
    print(first, operator, second, "=", result)
elif(operator == '*'):
    result = float(first) * float(second)
    print(first, operator, second, "=", result)
elif(operator == '/'):
    result = float(first) / float(second)
    print(first, operator, second, "=", result)
else:
    print("Please enter a valid operator (+, -, * or /)")