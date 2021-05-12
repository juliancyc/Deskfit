# Setting up variables
def numTestPositive(Dim):
    while True:
        try:
            val = int(Dim)
            if val < 0:  # if not a positive int print message and ask for input again
                print("Sorry, input must be a positive number, try again")
                continue
            break
        except ValueError:
            print("Please enter an positive number")
    return val

roomSide1 = numTestPositive(float(input("Please enter the first dimension of the room in US ft.")))
roomSide2 = numTestPositive(float(input("Please enter the second dimension of the room in US ft.")))
list = sorted([roomSide1, roomSide2])

# For future adjustment of Non-orthogonal room
roomWidth = list[0]
roomLength = list[1]

# Desk size
#deskSidesShort = float(input("Please enter the depth of the desk in US inch"))
#deskSideLong = float(input("Please enter the width of the desk in US inch"))
deskDepth = 24/12
deskWidth = 80/12
aisleWidth = 4
minUnit = deskDepth + aisleWidth + deskDepth

#Function

def deskRemainder(roomDim, deskDim):
    return divmod(roomDim, deskDim)


#Main
longSideCount = deskRemainder(roomWidth, deskWidth)
shortSideUnitCount = deskRemainder(roomLength, minUnit)
roughTotal = longSideCount[0] * shortSideUnitCount[0] * 2
aisleDeskCount = 0

if shortSideUnitCount[0] > 1:
    aisleDeskCount = shortSideUnitCount[0] * 2 - aisleWidth//deskWidth

elif shortSideUnitCount[0] <= 1:
    aisleDeskCount = 0

if shortSideUnitCount[1] >= aisleWidth + deskDepth: #For a row with no shared aisle.
    roughTotal = roughTotal + longSideCount[0]

if longSideCount[1] + deskWidth >= aisleWidth + deskDepth:  #For an extra table on the side.
    roughTotal = roughTotal + shortSideUnitCount[0] - 1

deskCount = roughTotal - aisleDeskCount

print("You can fit " + str(int(deskCount)) + " desk in this room.")
print("LongSideCount: " + str(longSideCount[0]), "Remainder: " + str(longSideCount[1]))
print("shortSideUnitCount: " + str(shortSideUnitCount[0]), "Remainder: " + str(shortSideUnitCount[1]))
print("aisleDeskCount: " + str(aisleDeskCount))
