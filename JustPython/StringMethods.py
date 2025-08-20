# Program to demo string functions

text = "Its an aMMazing dAy"
condition_text = "1An@"

print(text.title())
print(text.upper())
print(text.lower())
print(text.swapcase())

for c in condition_text:
    if c.isdigit():
        print(f"{c} is number")
    elif c.isalpha():
        print(f"{c} is alphabet")
    else:
        print(f"{c} is special character")
