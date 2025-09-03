text = "Kotlin Quick Start Guide"

frequency = dict()

for i in (text.lower()).replace(' ', ''):
    if i in frequency.keys():
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)