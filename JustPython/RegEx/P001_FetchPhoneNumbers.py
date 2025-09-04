import re 

pattern = r"\b\d{10}\b"
text = "John's contact number is 9007826722 and his wife's number is 78782877222. Emergency contact is 4662887282"

print(re.findall(pattern, text))

# output
# ['9007826722', '4662887282']