# dfs에서 시간초과가 날것 같다면? 무조건 bfs를 생각해보는 습관을 들이자!
# dfs, bfs 둘다 잘 쓸 수 있는 사람이 되자

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int , input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
day = 0

dq = deque()
new_q = deque()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if(arr[i][j] == 1):
            new_q.append([i,j])

dq.append(new_q)
while dq:
    q = dq.popleft()
    new_q = deque()
    while q:
        k = q.popleft()
        for i in range(4):
            nx = k[0] + dx[i]
            ny = k[1] + dy[i]
            if(nx>=0 and ny>=0 and nx<n and ny<m):
                if(arr[nx][ny] == 0):
                    arr[nx][ny] = 1
                    new_q.append([nx,ny])
    if(new_q):
        day += 1
        dq.append(new_q)

check = True
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if(arr[i][j] == 0):
            check = False

if(check == True):
    print(day)
else:
    print(-1)