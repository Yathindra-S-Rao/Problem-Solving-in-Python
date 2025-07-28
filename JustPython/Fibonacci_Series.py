number = int(input('Enter a number to print fibonacci series : '))
counter = 0
series = list()

while counter < number:
    if counter == 0:
        series.append(0)
    elif counter == 1:
        series.append(1)
    else:
        series.append(series[counter - 1] + series[counter - 2])
    counter += 1

print(series)
