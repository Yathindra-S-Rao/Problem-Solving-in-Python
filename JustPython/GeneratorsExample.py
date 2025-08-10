Demo Generators

def generator(number):
    i = 0
    while i < number:
        yield i
        i += 1

gen = generator(6)

for n in gen:
    print(n)