spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

# This causes the sort() function to treat all the items in the list
# as if they were lowercase
spam.sort(key=str.lower)
print(spam)
