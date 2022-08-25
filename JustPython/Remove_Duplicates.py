#       Program to remove duplicates in a list
#       1. We can convert the list into a set and convert it back into a list
#       2. We can create an empty list and travese with the first list 

#       First method
list1 = [1, 2, 3, 3]
set1 = set(list1)
list1 = list(set1)

#       Second method
list2 = [1, 2, 2, 3, 1, 5, 6, 3]
list3 = []

for i in list2:
    if i not in list3:
        list3.append(i)

print(list3)
