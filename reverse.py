word = input("Enter a string: ")

reverse = ""

for letter in word:
    reverse = letter + reverse

print("Reversed string:", reverse)