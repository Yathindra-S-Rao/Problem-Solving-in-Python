#   Demonstration of maps and filters

sq = lambda a: a ** 2
li = list(map(sq, range(5)))
print(li)

even = lambda a: a % 2 == 0
even_li = list(filter(even, range(30)))
print(even_li)
