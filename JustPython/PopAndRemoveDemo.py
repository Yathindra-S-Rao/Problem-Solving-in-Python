list1 = [1, 3, 4, 7, 8, 1, 4]

print(list1.pop())
print(list1.remove(7))

print(list1)
list1.remove(1)
print(list1)

'''
pop method returns the popped element and it deletes the last element in the list
remove method returns None and removes first occurance of the element

output:
4
None
[1, 3, 4, 8, 1]
[3, 4, 8, 1]

'''