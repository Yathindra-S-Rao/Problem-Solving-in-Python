# Program to reverse the words in the string


text = 'This is an amazing day'

reversed_text = ' '.join(i for i in text.split()[::-1])
print(reversed_text)
