# Program to replace couple of words in the given text

text = 'It is my work and your assignment'
temp = text.split(' ')
size = len(temp)

for i in range(size):
    if temp[i].strip() == 'my':
        temp[i] = 'your'
    elif temp[i].strip() == 'your':
        temp[i] = 'my'

result = ' '.join(temp)
print('Input Text is :\n',text)
print('Output Text is :\n',result)

# Output
# Input Text is :
# It is my work and your assignment
# Output Text is :
# It is your work and my assignment
