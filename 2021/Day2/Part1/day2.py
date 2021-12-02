#Jeremy Davison AoC 2021 Challenge Responses
#https://adventofcode.com/2021/day/2/
#https://github.com/jeremyrobertdavison

#Open the File with my Input from AoC

input = open('input.txt', 'r')

Lines = input.readlines()

#Since we are basically using a cartesian plane set x and y axis to 0

x = 0
y = 0

#Drawing this out helped identify what the correct direction was doing. Up is subtracting because you are gaining a negative depth, by the distance value.
#We pull these values by reading in the line and spliting it, which does by space as a seperater, default.

for line in Lines:
    dir, dist = line.split()
    if dir == "forward":
        x += int(dist)
    elif dir == "down":
        y += int(dist)
    elif dir == "up":
        y -= int(dist)
    else:
        break

#Finally, we multiply the x and y values we have aggregated and we get a z value. Print Z for the user.

z = x * y

print("The value of the multipliplied x and y coordinates is: " + str(z))