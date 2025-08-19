# Program to check the valid indian phone numbers

import re 

pattern = r'^\+91\d{10}$'

text = ['+9190023894389', '+538974683', '+919090783782', '+2189894893', '+917347937']
result = dict()

for each in text:
    result[each] = "Valid" if re.fullmatch(pattern, each) else "Invalid"
    
for k in result.keys():
    print(f'{k} is {result[k]}')
