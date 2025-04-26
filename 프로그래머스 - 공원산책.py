park = ["OSO","OOO","OXO","OOO"]	
routes= ["E 2","S 3","W 1"]	


h = len(park)
w = len(park[0])

parkList = []
startPoint = []
i = 0
for parkString in park:
    x = list(parkString)
    if(x.count('S') > 0):
        startPoint.append(i)
        startPoint.append(x.index('S'))
    parkList.append(list(parkString))
    i += 1


for route in routes:
    routeList = route.split(" ")
    goStatus = True
    for x in range(1, int(routeList[1])+1):
        if(routeList[0] == 'E'):
            if(startPoint[1] + x > w-1
            or (parkList[startPoint[0]][startPoint[1] + x] == 'X')):
                goStatus = False
                break
        elif (routeList[0] == 'S'):
            if(startPoint[0] + x > h-1
            or (parkList[startPoint[0] + x][startPoint[1]] == 'X')):
                goStatus = False
                break
        elif (routeList[0] == 'N'):
            if(startPoint[0] - x < 0
            or (parkList[startPoint[0] - x][startPoint[1]] == 'X')):
                goStatus = False
                break
        elif(routeList[0] == 'W'):
            if(startPoint[1] - x < 0
            or (parkList[startPoint[0]][startPoint[1] - x] == 'X')):
                goStatus = False
                break
    if(goStatus == True):
        if(routeList[0] == 'E'):
            startPoint[1] = startPoint[1] + int(routeList[1])
        elif (routeList[0] == 'S'):
            startPoint[0] = startPoint[0] + int(routeList[1])
        elif (routeList[0] == 'N'):
            startPoint[0] = startPoint[0] - int(routeList[1])
        elif(routeList[0] == 'W'):
            startPoint[1] = startPoint[1] - int(routeList[1])


print(startPoint)