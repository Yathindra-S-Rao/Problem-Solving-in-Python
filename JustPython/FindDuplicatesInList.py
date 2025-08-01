given = [1, 2, 3, 4, 2, 1, 3]
duplicates = list()

for i in given:
    if given.count(i) > 1 and (i not in duplicates):
        duplicates.append(i)

print(duplicates)
