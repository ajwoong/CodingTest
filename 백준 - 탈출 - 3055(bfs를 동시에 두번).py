# bfs를 동시에 두번하는 문제였다.
# 물의 측면, 비버의 측면에서 bfs를 하는 문제였는데 구현방식이 까다롭지 않았는데 생각보다 헷갈렸다
# 물을 한턴, 비버를 한턴 각각 움직여주는게 이 두 bfs를 동시에 처리하는 문제의 핵심이었다.

from collections import deque

r, c = map(int, input().split())
route_map = [list(input()) for _ in range(r)]

dq_bieber = deque()
bieber_visited = [[False] * c for _ in range(r)]

dq_water = deque()
water_visited = [[False] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if route_map[i][j] == 'S':
            dq_bieber.append((i, j, 0))
            bieber_visited[i][j] = True
        elif route_map[i][j] == '*':
            dq_water.append((i, j))
            water_visited[i][j] = True

nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]

while dq_bieber:
    for _ in range(len(dq_water)):
        x, y = dq_water.popleft()
        for i in range(4):
            nx_, ny_ = x + nx[i], y + ny[i]
            if 0 <= nx_ < r and 0 <= ny_ < c:
                if not water_visited[nx_][ny_] and route_map[nx_][ny_] == '.':
                    route_map[nx_][ny_] = '*'
                    water_visited[nx_][ny_] = True
                    dq_water.append((nx_, ny_))

    for _ in range(len(dq_bieber)):
        x, y, t = dq_bieber.popleft()
        for i in range(4):
            nx_, ny_ = x + nx[i], y + ny[i]
            if 0 <= nx_ < r and 0 <= ny_ < c:
                if route_map[nx_][ny_] == 'D':
                    print(t + 1)
                    exit()
                if route_map[nx_][ny_] == '.' and not bieber_visited[nx_][ny_]:
                    bieber_visited[nx_][ny_] = True
                    dq_bieber.append((nx_, ny_, t + 1))

print("KAKTUS")