#Jeremy Davison AoC 2021 Challenge Responses

#Open the File with my Input from AoC

input = open('input.txt', 'r')

Lines = input.readlines()

#First Value From My Input and Set Count to Zero
base = 156
count = 0

#Creat For Loop to Iterate Through lines of the File:

for line in Lines:

    #If the Line is less than the base then we know the Sonar value is lower in depth than current depth. Increase count by 1 to catch.

    if int(line) > base:

        count = count + 1

    #Set the new baesline to the current depth which is the line value.

    base = int(line)

#print the count to show the iteration as we go through the file

print("Count: " + str(count))
