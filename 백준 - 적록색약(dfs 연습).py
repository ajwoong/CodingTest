# dfs를 통해서 구역 탐색하는 문제를 다시 복기했다
# 재귀를 활용하는 것이 어색했지만 금방 보니까 다시 이해가 갔다
# 구역을 탐색하는 문제는 이제 익숙하게 풀 것 같다. 

from copy import deepcopy

field = ["RRRBB",
        "GGBBB",
        "BBBRR",
        "BBRRR",
        "RRRRR"]

fieldList= []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
countBlue = 0
countRed = 0
countGreen = 0
countRedAndGreen = 0
countBlueJug = 0

for x in field:
    fieldList.append(list(x))

jugFieldList = deepcopy(fieldList)


def dfsFindBlue(a, b):

    global countBlue

    if(a<0 or b<0 or a>=len(fieldList) or b >= len(fieldList[0])):
        return
    
    
    if(fieldList[a][b] == 'B'):
        fieldList[a][b] = 'X'
        countBlue += 1
        for x in range(4):
            dfsFindBlue(a+dx[x], b+dy[x])

def dfsFindRed(a, b):

    global countRed

    if(a<0 or b<0 or a>=len(fieldList) or b >= len(fieldList[0])):
        return
    
    
    if(fieldList[a][b] == 'R'):
        fieldList[a][b] = 'X'
        countRed += 1
        for x in range(4):
            dfsFindRed(a+dx[x], b+dy[x])

def dfsFindGreen(a, b):

    global countGreen

    if(a<0 or b<0 or a>=len(fieldList) or b >= len(fieldList[0])):
        return
    
    
    if(fieldList[a][b] == 'G'):
        fieldList[a][b] = 'X'
        countGreen += 1
        for x in range(4):
            dfsFindGreen(a+dx[x], b+dy[x])

def dfsFindRedAndGreen(a, b):

    global countRedAndGreen

    if(a<0 or b<0 or a>=len(jugFieldList) or b >= len(jugFieldList[0])):
        return
    
    
    if(jugFieldList[a][b] == 'G' or jugFieldList[a][b] == 'R'):
        jugFieldList[a][b] = 'X'
        countRedAndGreen += 1
        for x in range(4):
            dfsFindRedAndGreen(a+dx[x], b+dy[x])

def dfsFindBlueJug(a, b):

    global countBlueJug

    if(a<0 or b<0 or a>=len(jugFieldList) or b >= len(jugFieldList[0])):
        return
    
    
    if(jugFieldList[a][b] == 'B'):
        jugFieldList[a][b] = 'X'
        countBlueJug += 1
        for x in range(4):
            dfsFindBlueJug(a+dx[x], b+dy[x])


ans = []
for x in range(len(fieldList)):
    for y in range(len(fieldList[0])):
        if(fieldList[x][y] == "B"):
            dfsFindBlue(x,y)
            ans.append(countBlue)
            countBlue = 0
        elif(fieldList[x][y] == "R"):
            dfsFindRed(x,y)
            ans.append(countRed)
            countRed = 0
        elif(fieldList[x][y] == "G"):
            dfsFindGreen(x,y)
            ans.append(countGreen)
            countGreen = 0

jugAns = []
for x in range(len(jugFieldList)):
    for y in range(len(jugFieldList[0])):
        if(jugFieldList[x][y] == "B"):
            dfsFindBlueJug(x,y)
            jugAns.append(countBlueJug)
            countBlueJug = 0
        elif(jugFieldList[x][y] == "R" or jugFieldList[x][y] == "G"):
            dfsFindRedAndGreen(x,y)
            jugAns.append(countRedAndGreen)
            countRedAndGreen = 0

print(len(ans), len(jugAns))