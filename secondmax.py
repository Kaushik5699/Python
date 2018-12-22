vowels = ['a','e','i','o','u']
word = input()
found = {}
print(found)
for letter in word:
    if letter in vowels:
        found[letter] =+ 1
print(found)
