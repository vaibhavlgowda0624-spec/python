text = input("Enter text: ")

numbers = []

for character in text:
    if character.isdigit():
        numbers.append(character)

print("Numbers:", numbers)
