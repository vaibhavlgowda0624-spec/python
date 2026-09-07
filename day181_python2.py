numbers = [2, 5, 7, 2, 8, 5, 9, 7]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate Elements:", duplicates)
