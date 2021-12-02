#Jeremy Davison AoC 2015 Challenge Responses
#https://adventofcode.com/2015/day/1/
#https://github.com/jeremyrobertdavison

#Open the File with my Input from AoC

input = open('input.txt', 'r')

Lines = input.readlines()

totalArea = 0

for line in Lines:
    l,w,h = line.split("x")
    area = 2*int(l)*int(w) + 2*int(w)*int(h) + 2*int(h)*int(l)
    totalArea += area

print("The Elves would need " + str(totalArea) + " square feet of paper!")

#1598415,