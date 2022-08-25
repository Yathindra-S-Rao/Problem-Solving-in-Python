#       program to fetch the string which contains symbols in between

input_string = input("Enter a string with symbols : ")
output_string = ""

for i in input_string:
    if i.isalpha() or i.isdigit() or i.isspace():
        output_string += "".join(i)

print(output_string)
