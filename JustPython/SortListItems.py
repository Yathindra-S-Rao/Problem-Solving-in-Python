items = [3, 41, 24, 765, 13, 0]
sorted_list = list()
temp = None
ind = None

for item in range(len(items)):
    temp = min(items)
    ind = items.index(temp)
    sorted_list.append(temp)
    items.pop(ind)

print(sorted_list)
