sentence = input("Enter sentence: ")

words = sentence.split()

result = {}

for word in words:
    result[word] = len(word)

print(result)
