first = input("Enter first word: ").lower()
second = input("Enter second word: ").lower()

if sorted(first) == sorted(second):
    print("Anagram")
else:
    print("Not an Anagram")
