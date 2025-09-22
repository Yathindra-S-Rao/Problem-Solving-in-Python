given = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
result = list()


def delist(lst):
    for i in lst:
        if type(i) != list:
            result.append(i)
        else:
            delist(i)


delist(given)
print(result)
