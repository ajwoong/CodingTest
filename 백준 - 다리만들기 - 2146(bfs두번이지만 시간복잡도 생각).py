# 이 문제의 접근 과정은 다음과 같다.
# 1. 영토를 넘버링해서 분리(bfs)
# 2. 영토끼리 다리를 잇는데 최소 거리 구하기(bfs)

# 근데 bfs를 두번 대규모로 하니 시간초과가 발생했다
# 해당 문제를 해결하기 위해서는 2번과정에서 영토의 가장자리인 부분만 좌표를 꺼내서 bfs해주는 것이었다.
# 앞으로 시간초과가 나지 않도록 잘 계산해서 최적화하는 법을 생각해야겠다.

from collections import deque
import math
import sys
input = sys.stdin.readline

n = int(input())
world = []

for i in range(n):
    arr = list(map(int,input().split()))
    world.append(arr)

world_num = 2
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    for j in range(n):
        if(world[i][j] == 1):
            dq = deque()
            dq.append((i,j))
            visited = set()
            visited.add((i, j))
            world[i][j] = world_num 

            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if(0<=nx<n and 0<=ny<n and world[nx][ny] != 0):
                        if((nx,ny) not in visited):
                            world[nx][ny] = world_num
                            visited.add((nx,ny))
                            dq.append((nx,ny))

            world_num += 1

answer = math.inf

for label in range(2, world_num):
    dq = deque()
    visited = set()

    for i in range(n):
        for j in range(n):
            if world[i][j] == label:
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < n and world[ni][nj] == 0:
                        dq.append((i, j, 0))
                        visited.add((i, j))
                        break

    while dq:
        x, y, cost = dq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if world[nx][ny] == 0: 
                    visited.add((nx, ny))
                    dq.append((nx, ny, cost + 1))
                elif world[nx][ny] != label:
                    answer = min(answer, cost)
                    dq.clear() 
                    break

print(answer)