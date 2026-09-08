numbers = [64, 25, 12, 22, 11]

for i in range(len(numbers)):
    minimum = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[minimum]:
            minimum = j

    numbers[i], numbers[minimum] = numbers[minimum], numbers[i]

print("Sorted List:", numbers)
