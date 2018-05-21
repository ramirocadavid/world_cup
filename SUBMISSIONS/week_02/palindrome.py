# Request name
name = input("Please enter your first name (please enter only one word. If your name is composed\
 of more than one word, enter only the first): ")

## Invert name (using print(, end=""))
#count = len(name)
#while count > 0:
#    letter = name[count - 1:count]
#    if count == len(name):
#        print(letter.upper(), end="")
#    else:
#        print(letter.lower(), end="")
#    count -= 1

# Invert name (much shorter than the commented segment above)
count = len(name)
inv = ""
while count > 0:
    inv += name[count - 1: count]
    count -= 1
print(inv.capitalize())

# Check if name is a palindrome
if inv.lower() == name.lower():
    print("Palindrome!")
