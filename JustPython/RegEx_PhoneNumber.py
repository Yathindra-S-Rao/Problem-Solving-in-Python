#   Verification of valid phone number

import re

phone = input("Enter Phone number : ")
pattern = r"^[841]+\d{7}"

if re.fullmatch(pattern, phone):
    print("Valid phone number")
else:
    print("Phone number isn\'t valid")
