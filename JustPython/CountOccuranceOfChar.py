# Program to demo string functions

text = "aaabbccss"
result = ""
start = 0
temp = text + " "

while start < len(text):
    temp = temp[start:]
    print("temp=", temp)
    counter = 0
    if len(text) != 0:
        char = temp[0]
        for c in temp:
            if c == char:
                counter += 1
            else:
                start = counter
                result = result + str(counter) + char
                break


print(result)
