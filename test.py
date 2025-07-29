from collections import deque

array = []
answer_array = [[1,2,3],[4,5,6],[7,8,0]]

for i in range(3):
    new_array = list(map(int,input().split()))
    array.append(new_array)

dq = deque()

for i in range(3):
    for j in range(3):
        if(array[i][j] == 0):
            dq.append((i,j,0))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

while dq:
    x, y, t = dq.popleft()
    for i in range(4):
        nx, ny = x+ dx[i], y+dy[i]
        if(0<=nx<3 and 0<=ny<3):
            if(answer_array[x][y] == array[nx][ny]):
                dq.append((nx,ny,t+1))
                p = array[nx][ny]
                array[x][y] = p
                array[nx][ny] = 0
                break


for i in range(3):
    for j in range(3):
        if(array[i][j] != answer_array[i][j]):
            print(-1)
            exit()

print(t)
