#Jeremy Davison AoC 2021 Challenge Responses
#https://adventofcode.com/2021/day/3/
#https://github.com/jeremyrobertdavison

#Open the File with my Input from AoC

#Note to myself: This was done very quickly, and could be cleaned up. We should only need a single bit counter function and a function can be used to convert binary and base 10. The reporting strings at the end should be moved to one line

input = open('input.txt', 'r')

Lines = input.readlines()

#Create functions to return which is higher, given the Lines from the file and the position in the binary string

def bitCounterGamma(Lines, pos):
    count0 = 0
    count1 = 0
    for line in Lines:
        if line[pos] == "0":
            count0 += 1
        elif line[pos] == "1":
            count1 += 1
        else:
            print("ERROR")
    if count0 > count1:
        return 0
    else:
        return 1

def bitCounterEpsilon(Lines, pos):
    count0 = 0
    count1 = 0
    for line in Lines:
        if line[pos] == "0":
            count0 += 1
        elif line[pos] == "1":
            count1 += 1
        else:
            print("ERROR")
    if count0 < count1:
        return 0
    else:
        return 1

#Set gamma and epsilon variables and use the function to return a full binary string representing which is higher in count between 0 and 1

gamma = ''

for i in range(0,12):
    x = str(bitCounterGamma(Lines,i))
    gamma = gamma + x

epsilon = ''

for i in range(0,12):
    y = str(bitCounterEpsilon(Lines,i))
    epsilon = epsilon + y

#Convert the strings between binary and base 10. Then perform the math and report back the answer.

print("Gamma in Binary is: " + gamma)

gammaBin = int(gamma, 2)

print("Gamma in Decimal is: " + str(gammaBin))

print("Epsilon in Binary is: " + epsilon)

epsilonBin = int(epsilon, 2)

print("Epsilon in Decimal is: " + str(epsilonBin))

answer = epsilonBin * gammaBin

print("The answer is: " + str(answer))