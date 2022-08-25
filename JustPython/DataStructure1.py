# Data Structures in Python
# List methods
# Adding elements method append, insert and Extend
# Deleting elements method remove, pop() and clear()

list1 = list()
for i in range(0, 40, 10):
    list1.append(i)
print(list1)

list1.insert(0, 5)
print(list1)

list2 = list1.copy()
list1.extend(list1)
print(list1)

list1.pop()
print(list1)
print(list1.pop(4))             #   returns popped element
print(list1)
print(list1.remove(20))     #   returns  None

list1.clear()
print(list1)
print(list2)

#   Swapping
list2[0], list2[1] = list2[1], list2[0]
print("Swapped ",list2)

print(len(list2))
print(list2.index(20))
