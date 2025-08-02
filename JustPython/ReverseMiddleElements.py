# Program to Reverse only the middle elements of the list by leaving the first and last two elements in their place
# @author: Yathindra S.


Given = [1, 2, 3, 4, 5, 6, 7, 8]
op = list()

for c in range(0, len(Given)):
    if c < 2:
        op.append(Given[c])
    elif c >= len(Given)-2:
        op.append(Given[c])
    else:
        op.append(Given[-1*(c+1)])
        
print(op)