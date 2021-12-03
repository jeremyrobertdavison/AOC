#Jeremy Davison AoC 2021 Challenge Responses
#https://adventofcode.com/2021/day/1/
#https://github.com/jeremyrobertdavison

#Open the File with my Input from AoC

#Note to myself: This was done very quickly, and could be cleaned up. We should only need a single bit counter function and a function can be used to convert binary and base 10. The reporting strings at the end should be moved to one line

input = open('input.txt', 'r')

Lines = input.readlines()

#Create functions to return which is higher, given the Lines from the file and the position in the binary string

o2 = Lines
co2 = Lines

#Create functions to count for 02 and C02 values, returning either the 0 or 1.

def bitCounter02(pos, BinaryLines):

    zero = 0

    one = 0

    for i in BinaryLines:

        if i[pos] == "0":

            zero += 1

        else:

            one += 1

    if one >= zero:

        return 1

    else:

        return 0

def bitCounterC02(pos, BinaryLines):

    zero = one = 0

    for i in BinaryLines:

        if i[pos] == "0":

            zero += 1

        else:

            one += 1

    if one >= zero:

        return 0

    else:

        return 1

#function to test that the bitcounter results match the binary set

def recalc(comp, pos, BinaryLines):

    if len(BinaryLines) > 1:

        BinaryLines_ReCalc = [i for i in BinaryLines if int(i[pos]) == comp]

        return BinaryLines_ReCalc

    else:

        return BinaryLines

#Perform the count & calculations
for x in range(12):
    o2 = recalc(bitCounter02(x, o2), x, o2)
    co2 = recalc(bitCounterC02(x, co2), x, co2)

cO2Total = int(co2[0], 2)

O2Total = int(o2[0], 2)

answer = cO2Total * O2Total

#Report the answer to the screen

print("The C02 Value is: " + str(cO2Total))

print("The O2 Value is: " + str(O2Total))

print("The Answer is: " + str(answer))