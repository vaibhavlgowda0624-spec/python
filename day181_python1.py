numbers = [10, 20, 30, 40, 50, 60, 70]
target = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("Found" if found else "Not Found")
