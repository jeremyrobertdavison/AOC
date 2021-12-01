#Jeremy Davison AoC 2021 Challenge Responses
#https://adventofcode.com/2021/day/1/
#https://github.com/jeremyrobertdavison

#Open the File with my Input from AoC

input = open('input.txt', 'r')

Lines = input.readlines()

#Set variables we will use to 0
count = 0
base = 0
new = 0

#For i in range of the total number of lines.

for i in range (len(Lines) - 2):

    #new = a sum of line at index [i] in Lines plus the next two lines (i + 1) and (i + 2), by adjusting the index value by 1 and then 2.

    new = int(Lines[i]) + int(Lines[i+1]) + int(Lines[i+2])

    #Compare base and new value. If new is greater than baseline then count increases as we have had an increase in depth.

    if base > 0 and new > base:

        count += 1

    #Set the new baseline to the new value to establish the new current depth.

    base = new

#Print the final answer.

print(count)