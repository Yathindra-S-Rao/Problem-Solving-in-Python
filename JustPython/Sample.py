''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    virus_comp = input()
    no_of_people = input()
    people = list()
    for person in range(int(no_of_people)):
        people.append(input())

    for person in people:
        temp = 0
        index = -1
        for i in range(len(person)):
            if index == -1:
                index = virus_comp.find(person[i])
            else:
                index = virus_comp.find(person[i], index)

    print(index)
main()

