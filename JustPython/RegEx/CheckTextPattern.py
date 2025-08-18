import re

text = "Wipro@2023"
pattern = r"^[A-Za-z]+[@][0-9]+$"

print(re.search(pattern, text))