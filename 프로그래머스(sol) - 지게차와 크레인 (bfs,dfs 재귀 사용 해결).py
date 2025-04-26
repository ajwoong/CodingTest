# bfs, dfs 개념을 사용하고 재귀를 이용하는 문제였다
# 취약한 부분이라 생각하지 말고 굉장히 잘할 수 있는 사람이 되어야겠다. 앞으로 더 많이 나올텐데 bfs,dfs를 차라리 확실히 공부해서 다시 준비하자

from collections import deque

def checkMinusOne(newStorage, x, y):
        dx, dy = [0,0,1,-1], [1,-1, 0, 0]
        minusOne = False

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if(newStorage[nx][ny] == '-1'):
                newStorage[x][y] = '-1'
                minusOne = True
                break

        if minusOne:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (newStorage[nx][ny] == '0'):
                    newStorage[nx][ny] = '-1'
                    checkMinusOne(newStorage, nx, ny)

def solution(storage, requests):

    answer = 0
    newStorage = deque()

    for x in storage:
        stringList = list(x)
        stringList = deque(stringList)
        stringList.appendleft("-1")
        stringList.append("-1")
        newStorage.append(list(stringList))

    newStorage.appendleft(["-1" for x in range(len(storage[0]) + 2)])
    newStorage.append(["-1" for x in range(len(storage[0]) + 2)])
    newStorage = list(newStorage)


    h = len(newStorage)
    l = len(newStorage[0])

    for request in requests:
        if(len(request) == 1):
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            index = []
            for x in range(1,h-1):
                for y in range(1,l-1):
                        if(newStorage[x][y] == request):
                            for i in range(4):
                                nx, ny = x + dx[i], y + dy[i]
                                if newStorage[nx][ny] == '-1':
                                    index.append((x,y))
                                    break
            for x,y in index:
                newStorage[x][y] = '-1'
                checkMinusOne(newStorage, x, y)

        if(len(request) == 2):
            index = []
            for x in range(1,h-1):
                for y in range(1,l-1):
                        if(newStorage[x][y] == request[0]):
                            newStorage[x][y] = '0'
                            checkMinusOne(newStorage, x, y)

    for x in range(1, h-1):
        for y in range(1, l-1):
            if newStorage[x][y] not in ["-1", "0"]:
                answer+=1
    
    return answer