import re
#       Program to replace numerals(0-9) with string of numbers in the given string

number_values = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
given_string = str(input("Enter a string with numerals : "))
given_string = given_string.split()
output_string = ""

for i in given_string:
    if i in str(number_values):
        output_string += "".join(number_values[int(i)]) + " "
    else:
        output_string += "".join(i) + " "

print(output_string)
