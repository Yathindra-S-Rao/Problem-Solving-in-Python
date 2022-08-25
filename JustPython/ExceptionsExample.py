#   Exceptions in Python

try:
    a, b = "Hello", 0
    c = a / b
except ZeroDivisionError:
    print("Zero Division error occured!")
except TypeError:
    print("Type error occured!")
finally:
    print("Program terminated successfully! (Finally block)")
