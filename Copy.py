import copy

spam = ['A', 'B', 'C', 'D']
cheese = spam
cheese[1] = 42
print(spam)
print(cheese)

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

spam = ['A', ['B1', 'B2', 'B3'], 'C', 'D']
cheese = copy.copy(spam)
cheese[1][1] = 42
print(spam)
print(cheese)

spam = ['A', ['B1', 'B2', 'B3'], 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1][1] = 42
print(spam)
print(cheese)
