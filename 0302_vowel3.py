# nums = [1, 2, 3, 4]
# print(nums)

# nums.remove(3)
# print(nums)

# nums.pop()
# print(nums)

# nums.pop(0)
# print(nums)

# nums.extend([3, 4])
# print(nums)

# nums.insert(0, 1)
# print(nums)

# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)

# for i in range(4):
#     plist.pop()

# plist.pop(0)
# plist.remove("'")
# plist

# first = [1, 2, 3, 4, 5]
# first

# second = first
# second

# second.append(6)
# second      # second에 append하면,
# first       # first에도 append됨.

# third = second.copy()
# third
# third.append(7)
# third
# second

# saying = "Don't Panic!"
# letters = list(saying)

# letters

# letters[0]
# letters[-1]

vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)        


