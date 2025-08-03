import re

text = 'abc@maybank.com, cs@maybank.com, god@gmail.com, fg@hmail.com'
emails = text.split(',')

filtered = list()
op = [i for i in emails if i.endswith('@maybank.com')]


for email in emails:
    if email.endswith('@maybank.com'):
         filtered.append(email)
print(filtered)
print(op)