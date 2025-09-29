text = "This this is an an ammazing thing"
words = text.split()
result = ""
i = 1
while i < len(words):
    if not(words[i-1].lower() == words[i].lower()):
        result = result +" "+ words[i-1]
    i += 1
  


print(result)