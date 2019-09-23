print("This is a line of text!")

print("This is a line of text!\n This is a second line!")

print("This is some \" text")

#This string is stored in variable
phrase = "String in a variable"
print(phrase)
print("\n" + phrase + " and concatenated string")

print(phrase.capitalize())

print(phrase.upper())

print(phrase.isupper())
print(phrase.islower())

# converts variable to uppercase and checks if its true
print(phrase.upper().isupper())

print(len(phrase))
print(phrase[2])

print(phrase.index("S"))
print(phrase.index("i"))

print(phrase)
print(phrase.replace("variable", "variable_replaced"))
