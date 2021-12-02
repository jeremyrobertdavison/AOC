#Jeremy Davison AoC 2015 Challenge Responses
#https://adventofcode.com/2015/day/1/
#https://github.com/jeremyrobertdavison

#Open the File with my Input from AoC

input = open('input.txt', 'r')

floor = 0

Lines = input.readlines()

firstHit = False

for line in Lines:
    for i in range(len(line)):
        if line[i] == "(":
            floor += 1
        elif line[i] == ")":
            floor -= 1
        if floor == -1 and firstHit == False:
            print("Basement entered at character: " + str(i + 1))
            firstHit = True

