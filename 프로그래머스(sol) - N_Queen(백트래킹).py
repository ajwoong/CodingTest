# 구현까지는 다 왔지만, deepcopy를 통해서 기존의 배열을 복사한 방법이 시간복잡도를 초과하게 만들었다
# deepcopy 말고 기존 배열에 변경사항이 있다면 그 변경사항만 원상복구 하는 방법을 사용하면 된다.

from copy import deepcopy

dx =[0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
count = 0

def update(x,y,n,maps):
    changes = []
    if(maps[x][y] == 0):
        changes.append((x,y,maps[x][y]))
        maps[x][y] = -1
        for k in range(8):
            nx = x
            ny = y
            while True:
                nx = nx + dx[k]
                ny = ny + dy[k]
                if(nx<0 or ny<0 or nx>=n or ny>=n):
                    break
                if maps[nx][ny] != 0:
                    continue
                changes.append((nx, ny, maps[nx][ny]))
                maps[nx][ny] = 1
    return changes

def nqueen(y, n, maps):
    global count
    if(y>=n):
        count += 1
        return
    
    for x in range(n):
        if(maps[x][y] == 0):
            changes = update(x,y,n,maps)
            nqueen(y+1,n,maps)
            for cx, cy, old_value in changes:
                maps[cx][cy] = old_value
    return


def solution(n):
    global count
    maps = [[0 for _ in range(n)] for _ in range(n)]
    nqueen(0, n, maps)
    return count