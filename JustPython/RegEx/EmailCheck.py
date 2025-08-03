import re

text = 'yathi@maybank.com, jan@maybank.com, kumar@gmail.com, kalyan@hotmail.com'
pattern = r'.+@maybank\.com'

emails = text.split()
results = [email.strip() for email in emails if re.match(pattern, email)]

print(results)
