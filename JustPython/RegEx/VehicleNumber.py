import re 

pattern = r"^KA\s*\d{2}\s*[A-Z]{2}\s*\d{4}$"
text = "KA 01 ME 1233"

print(re.match(pattern, text))