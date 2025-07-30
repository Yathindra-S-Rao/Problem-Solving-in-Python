text = "hello11 huli2681dhis"
g = sum(1 for n in text if n in "0123456789")
print(f"There are {g} numbers in {text}")