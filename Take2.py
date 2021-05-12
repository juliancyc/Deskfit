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
roomSide2 = numTestPositive(float(input("Please enter the second of the room in US ft.")))
list = sorted([roomSide1, roomSide2])

# For future adjustment of Non-orthogonal room
roomWidth = list[0]
roomLength = list[1]

# Desk size
#deskSidesShort = float(input("Please enter the depth of the desk in US inch"))
#deskSideLong = float(input("Please enter the width of the desk in US inch"))
deskDepth = 24/12
deskWidth = 48/12
aisleWidth = 4
minUnit = deskDepth + aisleWidth + deskDepth

#Function

def deskRemainder(roomDim, deskDim):
    return divmod(roomDim, deskDim)


#Main
lonSideCount = deskRemainder(roomWidth, deskWidth)
shortSideUnitCount = deskRemainder(roomLength, minUnit)
roughTotal = lonSideCount[0] * shortSideUnitCount[0] * 2
aisleDeskCount = shortSideUnitCount[0] * 2 - 1

if shortSideUnitCount[1] >= aisleWidth + deskDepth:
    roughTotal = roughTotal + lonSideCount[0]

deskCount = roughTotal - aisleDeskCount

print(lonSideCount,shortSideUnitCount,roughTotal,aisleDeskCount)
print(deskCount)