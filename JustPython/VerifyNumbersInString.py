# given = 'There are 10 apples in 5 baskets'
# temp = given.split(' ')
# l = list()
#
# def state(n):
#     return 'Even' if n % 2 == 0 else 'Odd'
#
# for i in temp:
#     if i.isnumeric():
#         l.append(int(i))
#
# ou = print(list(map(state, l)))
#

import re
given = 'There are 10 apples in 5 baskets'

number = list(map(int, re.findall(r'\d+', given)))
ou = ['Even' if i % 2 == 0 else 'Odd' for i in number]

print(ou)



