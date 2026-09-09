expression = input("Enter expression: ")

balance = 0
valid = True

for char in expression:
    if char == "(":
        balance += 1
    elif char == ")":
        balance -= 1

    if balance < 0:
        valid = False
        break

if balance != 0:
    valid = False

print("Balanced" if valid else "Not Balanced")
