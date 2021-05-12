# Setting up variables
while True:
    try:
        roomSide1 = float(input("Please enter the first dimension of the room in US ft."))
        roomSide2 = float(input("Please enter the second dimension of the room in US ft."))
        deskside1 = float(input("Please enter the first dimension of the desk in US inch"))
        deskside2 = float(input("Please enter the second dimension of the desk in US inch"))
        if roomSide1 * roomSide2 * deskside1 * deskside2 <= 0:
            print("Sorry, input must be a positive number, try again")
            continue
        break
    except ValueError:
        print("Please enter an positive number")

list = sorted([roomSide1, roomSide2])
roomWidth = list[1]
roomLength = list[0]

# Desk size
list2 = sorted([deskside1, deskside2])
deskDepth = list2[1]/12
deskWidth = list2[0]/12
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
vDeskCount = 0

if shortSideUnitCount[0] > 1:
    aisleDeskCount = shortSideUnitCount[0] * 2 - aisleWidth//deskWidth

elif shortSideUnitCount[0] <= 1:
    aisleDeskCount = 0

if shortSideUnitCount[1] >= aisleWidth + deskDepth: #Add a row at the wall if the last row can fit a table + aisle.
    roughTotal = roughTotal + longSideCount[0]

if longSideCount[1] >= deskDepth: #Add extra table on the side of double rows if the aisle is wide enough.
    vDeskCount = shortSideUnitCount[0] - 1
    roughTotal = roughTotal + vDeskCount

deskCount = roughTotal - aisleDeskCount

print("You can fit " + str(int(deskCount)) + " desk in this room.")
print("LongSideCount: " + str(longSideCount[0]), "Remainder: " + str(longSideCount[1]))
print("shortSideUnitCount: " + str(shortSideUnitCount[0]), "Remainder: " + str(shortSideUnitCount[1]))
print("aisleDeskCount: " + str(aisleDeskCount))
print("vDeskCount: " + str(vDeskCount))
