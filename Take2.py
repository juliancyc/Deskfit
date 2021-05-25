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
        list1 = sorted([roomSide1, roomSide2])
        if roomSide1 * roomSide2 * deskSide1 <= 0 or deskSide2 <=0 : #making sure the value is positive
            print("Sorry, input must be a positive number, try again")
            continue
        break
    except ValueError:
        print("Please enter an positive number")


roomWidth = list1[1]
roomLength = list1[0]

# Desk size
list2 = sorted([deskSide1, deskSide2])
deskDepth = list2[0]/12 #from inch to foot
deskWidth = list2[1]/12
aisleWidth = 4 #set to fix value but can be changed
minUnit = deskDepth + aisleWidth + deskDepth

#Function

def deskRemainder(roomDim, deskDim):
    return divmod(roomDim, deskDim)


#MainCalcs
longSideCount = deskRemainder(roomWidth, deskWidth)
shortSideUnitCount = deskRemainder(roomLength, minUnit)
roughTotal = longSideCount[0] * shortSideUnitCount[0] * 2
midRowCount = 0
aisleDeskCount = 0
vDeskCount = 0
loneRow = False #for future visualization
vDesk = False#for future visualization

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
    loneRow = True

if longSideCount[1] + math.ceil(aisleWidth/deskWidth)*deskWidth >= aisleWidth + deskDepth: #Add extra table on the side of double rows if the aisle is wide enough.
    vDeskCount = shortSideUnitCount[0] - 1
    roughTotal = roughTotal + vDeskCount
    vDesk = True

deskCount = roughTotal - aisleDeskCount

print("You can fit " + str(int(deskCount)) + " desk in this room.")

print(list1, list2)
print("LongSideCount: " + str(longSideCount[0]) + " desks", "Remainder: " + str(longSideCount[1]) + " ft")
print("shortSideUnitCount: " + str(shortSideUnitCount[0])+" Min Units", "Remainder: " + str(shortSideUnitCount[1]) + " ft")
print("aisleDeskCount: " + str(aisleDeskCount) + " desks")
print("vDeskCount: " + str(vDeskCount) + " vertical desks")



#Rhino Part (WIP)

model = rhino3dm.File3dm()
deskList = []
rowList = []
deskRoughTotal = []

#Room
roomPt = \
    [rhino3dm.Point3d(0.0, 0.0, 0.0),
     rhino3dm.Point3d(roomWidth, 0.0, 0.0),
     rhino3dm.Point3d(roomWidth, roomLength, 0.0),
     rhino3dm.Point3d(0.0, roomLength, 0.0),
     rhino3dm.Point3d(0.0, 0.0, 0.0)]

model.Objects.AddPolyline(roomPt)

'''
#Rhino:Take1  Desk Module to move/copy around 
while i >= 1:
    deskModule = \
    [rhino3dm.Point3d(0, 0, 0),
        rhino3dm.Point3d(deskWidth, 0, 0),
        rhino3dm.Point3d(deskWidth, deskDepth, 0),
        rhino3dm.Point3d(0, deskDepth, 0),
        rhino3dm.Point3d(0, 0, 0)]

    deskList.append(deskModule)
    i-=1
for m in desks:
    model.Objects.AddPolyline(m)


#Rhino Take2: Desk module + location calculation Ver1
while i >= 1:
    deskModule = \
    [rhino3dm.Point3d(i * deskWidth, j*(deskDepth + aisleWidth), 0),
        rhino3dm.Point3d((i - 1) * deskWidth, j*(deskDepth + aisleWidth + deskDepth), 0),
        rhino3dm.Point3d((i - 1) * deskWidth, j*(deskDepth + aisleWidth), 0),
        rhino3dm.Point3d(i * deskWidth, j*(deskDepth + aisleWidth + deskDepth), 0),
        rhino3dm.Point3d(i * deskWidth, j*(deskDepth + aisleWidth), 0)]

    deskList.append(deskModule)

    i -= 1

for m in deskList:
    model.Objects.AddPolyline(m)
'''

'''
#Rhino Take2: Desk module + location calculation Ver2
#"Maybe I can send in a list of points and solve everything in one For loop."

i = longSideCount[0]
j = shortSideUnitCount[0]
iList  = []
jList = []

while i >= 1:
    iList.append(i)
    i-=1

while j >= 1:
    jList.append(j)
    j-=1

deskPt = itertools.product(iList,jList) #produce a list of (row, column) location, and use it to generate all points needed for all desks

for v in deskPt:
    desk = [rhino3dm.Point3d((v[0]-1) * deskWidth, (v[1]-1) * (deskDepth) + (v[1]-1)*(aisleWidth+deskDepth), 0),
        rhino3dm.Point3d((v[0]) * deskWidth, (v[1]-1) * (deskDepth) + (v[1]-1)*(aisleWidth+deskDepth), 0),
        rhino3dm.Point3d((v[0]) * deskWidth, (v[1]) * (deskDepth) + (v[1]-1)*(aisleWidth+deskDepth), 0),
        rhino3dm.Point3d((v[0]-1) * deskWidth, (v[1]) * deskDepth + (v[1]-1)*(aisleWidth+deskDepth), 0),
        rhino3dm.Point3d((v[0]-1) * deskWidth, (v[1]-1) * deskDepth + (v[1]-1)*(aisleWidth+deskDepth), 0)]

    deskList.append(desk)

for d in deskList:
    model.Objects.AddPolyline(d)

model.Write('DeskPlan.3dm', 6) #Generating Rhino3dm
'''



#Rhino:Take3 Simple Functions WIP
#Desk Module
desk = \
    [[0, 0, 0],
     [deskWidth, 0, 0],
     [deskWidth, deskDepth, 0],
     [0, deskDepth, 0],
     [0, 0, 0]]

print(desk)

#Functions WIP, 

def addPointY(p,n):
    new_p = [p[0], p[1] + n, p[2]]
    return new_p

def addPointX(p,n):
    new_p = [p[0] + n, p[1], p[2]]
    return new_p


def gen_row(d,i):
    r = []
    l = [i * deskWidth for i in range (0,i)]
    for n in l:
        new_d = []
        for p in d:
            new_p = addPointX(p,n)
            new_d.append(new_p)
        r.append(new_d)
    return (r,l)


print(gen_row(desk, 5))
print(desk)

