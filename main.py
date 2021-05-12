# Setting up variables
#roomSideLong = float(input("Please enter the dimension of the longer side of the room in US ft."))
#roomSideShort = float(input("Please enter the dimension of the shorter side of the room in US ft."))

# For future adjustment of Non-orthogonal room
roomWidth = 20
roomLength = 15

# Desk size
#deskSidesShort = float(input("Please enter the depth of the desk in US inch"))
#deskSideLong = float(input("Please enter the width of the desk in US inch"))
deskDepth = 24/12
deskWidth = 48/12

#Calculation for large rooms without minimal conditions


def odd_layer(width, length):
    w_count = divmod(width-2*deskDepth,deskWidth)
    l_count = divmod(length-2*deskDepth,deskWidth)
    return 2*(w_count[0]+l_count[0])

total = odd_layer(roomWidth,roomLength)
print(total)
