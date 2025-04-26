import sys
sys.setrecursionlimit(10**6)

count = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y, maps):
    global count
    if(x<0 or x>= len(maps) or y<0 or y>=len(maps[0])):
        return

    if(maps[x][y] != 'X'):
        count += int(maps[x][y])
        maps[x][y] = 'X'
        for a in range(4):
            dfs(x + dx[a],y + dy[a], maps)

def solution(mapsString):
    maps = []
    global count 
    for x in mapsString:
        maps.append(list(x))

    answer = []
    for p in range(len(maps)):
        for q in range(len(maps[0])):
            if(maps[p][q] != 'X'):
                dfs(p,q, maps)
                answer.append(count)
                count = 0

    answer.sort()
    if(len(answer) == 0):
        return [-1]
    else:
        return answer

