import re

pattern = r"^([A-Z]{1}[a-z]*)(\s[A-Z]{1}[a-z]*)*$"
text_list = ["This Is Ammazing", "What a great day", "python Is Cool"]

for text in text_list:
    print(re.match(pattern, text))
    


# Output
    
<re.Match object; span=(0, 16), match='This Is Ammazing'>
None
None

#=== Code Execution Successful ===