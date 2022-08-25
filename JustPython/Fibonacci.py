# Fibonacci series using reccurssion

def Fun1(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: return Fun1(n-1) + Fun1(n-2)

num = int(input("Enter number of digits to print"))
for i in range(num):
    print(Fun1(i), end="\t")
