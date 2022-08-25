#   File handling in Python
#   each line of data will be appended with '\n' charecter at the end of the line
#   Note: the last line of data would not be containg the '\n' char at the end

file = open('Books.txt', 'r')
for each in file:
    if each[len(each)-1] == '\n':
        code = each[0] + str(len(each) -1)
    else:
        code = each[0] + str(len(each))
    print(code)

