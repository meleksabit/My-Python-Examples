# Shows the duplicate strings
my_list = ['a', 'b', 'c', 'd', 'd', 'm', 'm', 'n', 'o', 'z', 'z']
duplicates = []
for value in my_list:
    if my_list.count(value) > 1 and value not in duplicates:
        duplicates.append(value)
print(duplicates)
