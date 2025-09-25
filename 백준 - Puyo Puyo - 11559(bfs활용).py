# bfs 문제기도 하면서, 구현력이 상당히 필요한 문제였다.
# 요구사항을 보고 확실히 구현할 수 있는 능력을 더욱 길러야겠다.

from collections import deque

puyo_map = []

for i in range(12):
    puyo = list(input())
    puyo_map.append(puyo)

color = ['R', 'G', 'B', 'P', 'Y']
answer = 0

while True:
    puyo_cycle_end = True
    visited = [[0 for _ in range(6)] for _ in range(12)]
    to_pop = []  

    for c in color:
        dq = deque()
        for i in range(12):
            for j in range(6):
                c_count = 0
                where = []
                if(puyo_map[i][j] == c and visited[i][j] == 0):
                    dq.append((i,j))
                    where.append((i,j))
                    visited[i][j] = 1
                    c_count += 1
                    dx = [0,0,1,-1]
                    dy = [1,-1,0,0]

                    while dq:
                        x, y = dq.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if(0 <= nx < 12 and 0<= ny < 6):
                                if(puyo_map[nx][ny] == c and visited[nx][ny] == 0):
                                    dq.append((nx,ny))
                                    where.append((nx,ny))
                                    visited[nx][ny] = 1
                                    c_count += 1
                if(c_count >= 4):
                    puyo_cycle_end = False
                    to_pop.extend(where)  

    if puyo_cycle_end:
        break

    for x, y in to_pop:
        puyo_map[x][y] = '.'

    for col in range(6):
        stack = []
        for row in range(12):
            if puyo_map[row][col] != '.':
                stack.append(puyo_map[row][col])
                puyo_map[row][col] = '.'
        for i, val in enumerate(reversed(stack)):
            puyo_map[11 - i][col] = val

    answer += 1  

print(answer)