from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]	
dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0

target = []
def dfs(x, y, testLand):
    global count
    global target
    if(x<0 or y<0 or x>=len(testLand) or y>=len(testLand[0])):
        return
    
    if(testLand[x][y] == 1):
        count += testLand[x][y]
        target.append(y)
        testLand[x][y] = 0
        for k in range(4):
            dfs(x + dx[k], y +dy[k], testLand)


answer = [0] * len(land[0])
for y in range(len(land[0])):
    for x in range(len(land)):
        if(land[x][y] != 0):
            dfs(x, y, land)
            for x in set(target):
                answer[x] += count
            count = 0
            target = []
            
print(max(answer))

