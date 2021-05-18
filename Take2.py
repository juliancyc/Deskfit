import itertools
import math
import rhino3dm

# Setting up variables
while True:
    try:
        roomSide1 = float(input("Please enter the first dimension of the room in US ft."))
        roomSide2 = float(input("Please enter the second dimension of the room in US ft."))
        deskSide1 = float(input("Please enter the first dimension of the desk in US inch"))
        deskSide2 = float(input("Please enter the second dimension of the desk in US inch"))
        if roomSide1 * roomSide2 * deskSide1 * deskSide2 <= 0:
            print("Sorry, input must be a positive number, try again")
            continue
        break
    except ValueError:
        print("Please enter an positive number")

list1 = sorted([roomSide1, roomSide2])
roomWidth = list1[1]
roomLength = list1[0]

# Desk size
list2 = sorted([deskSide1, deskSide2])
deskDepth = list2[0]/12
deskWidth = list2[1]/12
aisleWidth = 4
minUnit = deskDepth + aisleWidth + deskDepth

#Function


def deskRemainder(roomDim, deskDim):
    return divmod(roomDim, deskDim)


#Main
longSideCount = deskRemainder(roomWidth, deskWidth)
shortSideUnitCount = deskRemainder(roomLength, minUnit)
roughTotal = longSideCount[0] * shortSideUnitCount[0] * 2
midRowCount = 0
aisleDeskCount = 0
vDeskCount = 0

if shortSideUnitCount[0] == 1 and shortSideUnitCount[1] >= aisleWidth + deskDepth:
    aisleDeskCount = (shortSideUnitCount[0]) * math.ceil(aisleWidth/deskWidth)

elif shortSideUnitCount[0] > 1 and shortSideUnitCount[1] >= aisleWidth + deskDepth:
    aisleDeskCount = ((shortSideUnitCount[0] - 1) * 2 + 1) * math.ceil(aisleWidth/deskWidth)

elif shortSideUnitCount[0] > 1 and shortSideUnitCount[1] < aisleWidth + deskDepth:
    aisleDeskCount = (shortSideUnitCount[0] - 1) * 2 * math.ceil(aisleWidth/deskWidth)

elif shortSideUnitCount[0] < 1:
    aisleDeskCount = 0

if shortSideUnitCount[1] >= aisleWidth + deskDepth: #Add a row at the wall if the last row can fit a table + aisle.
    roughTotal = roughTotal + longSideCount[0]

if longSideCount[1] + math.ceil(aisleWidth/deskWidth)*deskWidth >= aisleWidth + deskDepth: #Add extra table on the side of double rows if the aisle is wide enough.
    vDeskCount = shortSideUnitCount[0] - 1
    roughTotal = roughTotal + vDeskCount

deskCount = roughTotal - aisleDeskCount


#Rhino Part

#Room
model = rhino3dm.File3dm()

roomPt = \
    [rhino3dm.Point3d(0.0, 0.0, 0.0),
     rhino3dm.Point3d(roomSide2, 0.0, 0.0),
     rhino3dm.Point3d(roomSide2, roomSide1, 0.0),
     rhino3dm.Point3d(0.0, roomSide1, 0.0),
     rhino3dm.Point3d(0.0, 0.0, 0.0)]

model.Objects.AddPolyline(roomPt)

#Desks
desks = []


i = float(longSideCount[0])
j = float(shortSideUnitCount[0])

'''
while i >= 1:
    deskModule = \
    [rhino3dm.Point3d(i * deskWidth, 0, 0),
        rhino3dm.Point3d((i - 1) * deskWidth, 0, 0),
        rhino3dm.Point3d((i - 1) * deskWidth, deskDepth, 0),
        rhino3dm.Point3d(i * deskWidth, deskDepth, 0),
        rhino3dm.Point3d(i * deskWidth, 0, 0)]

    desks.append(deskModule)
    i-=1
for m in desks:
    model.Objects.AddPolyline(m)
'''

itertools.zip_longest()

while i >= 1:
    deskModule = \
    [rhino3dm.Point3d(i * deskWidth, j*(deskDepth + aisleWidth), 0),
        rhino3dm.Point3d((i - 1) * deskWidth, j*(deskDepth + aisleWidth + deskDepth), 0),
        rhino3dm.Point3d((i - 1) * deskWidth, j*(deskDepth + aisleWidth), 0),
        rhino3dm.Point3d(i * deskWidth, j*(deskDepth + aisleWidth + deskDepth), 0),
        rhino3dm.Point3d(i * deskWidth, j*(deskDepth + aisleWidth), 0)]

    desks.append(deskModule)

    i -= 1

for m in desks:
    model.Objects.AddPolyline(m)

model.Write('DeskPlan.3dm', 6)

print(desks)
print("You can fit " + str(int(deskCount)) + " desk in this room.")

print(list, list2)
print("LongSideCount: " + str(longSideCount[0]) + " desks", "Remainder: " + str(longSideCount[1]) + " ft")
print("shortSideUnitCount: " + str(shortSideUnitCount[0])+" Min Units", "Remainder: " + str(shortSideUnitCount[1]) + " ft")
print("aisleDeskCount: " + str(aisleDeskCount) + " desks")
print("vDeskCount: " + str(vDeskCount) + " vertical desks")

