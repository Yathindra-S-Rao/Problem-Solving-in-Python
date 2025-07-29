number = int(input("Enter a number:"))
factorial = 1
for I in range(1, number + 1):
    factorial *= I
    
print("Factorial = ", factorial)