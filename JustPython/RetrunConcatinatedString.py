#   SoloLearn challenge
#   Pass multiple arguments and return a concatenated string separated by "-"

def concatenate(*args):
    str1 = ""
    for i in args:
        str1 = str1 + "".join(i) + "-"
    return str1[0:-1]


print(concatenate("I", "Love", "Python", "!"))

val = "hello john!"
print(val.title())
print(val.casefold())
print(val.replace(' ', '-'))
