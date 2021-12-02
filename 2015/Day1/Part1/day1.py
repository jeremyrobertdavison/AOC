#Jeremy Davison AoC 2015 Challenge Responses
#https://adventofcode.com/2015/day/1/
#https://github.com/jeremyrobertdavison

#Open the File with my Input from AoC

input = open('input.txt', 'r')

floor = 0

Lines = input.readlines()

for line in Lines:
    print(len(line))
    for i in range(len(line)):
        if line[i] == "(":
            floor += 1
        elif line[i] == ")":
            floor -= 1

print("Floor: " + str(floor))
