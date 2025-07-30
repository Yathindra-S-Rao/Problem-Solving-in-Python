text = "amazing day"
g = sum(1 for c in text.lower() if c in "aeiou")
print(f'There are {g} Vovels in {text}')