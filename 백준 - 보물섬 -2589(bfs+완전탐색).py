# bfs와 완전탐색을 함께 구현하는 문제였다.

import sys
input = sys.stdin.readline

from collections import deque
n, m = map(int,input().split())

tmap = []
for i in range(n):
    line = list(input())
    tmap.append(line)

max_visited = 0
for i in range(n):
    for j in range(m):
        if(tmap[i][j] == 'L'):
            dq = deque()
            dq.append((i,j))

            visited = [[-1 for _ in range(m)] for _ in range(n)]
            visited[i][j] = 0
            max_visited = max(max_visited, visited[i][j])
            
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]

            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if(0 <= nx < n and 0 <= ny < m):
                        if(tmap[nx][ny] == 'L' and visited[nx][ny] == -1):
                            dq.append((nx,ny))
                            visited[nx][ny] = visited[x][y] + 1
                            max_visited = max(max_visited, visited[nx][ny])

print(max_visited)

            


