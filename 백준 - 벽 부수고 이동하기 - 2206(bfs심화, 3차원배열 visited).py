# 이 문제는 최단거리를 검색하는 문제로 bfs를 활용하는 것이었다.
# 하지만 기존에 문제와 달리 0만 지날수 있는 최소거리가아닌 1을 1번만 지날수있는 문제였다.
# 1을 1번만 지날수 있기때문에 1을 지났을때 해당 지점을 통과한 최소거리, 1을 지나지않았을때 해당 지점을 통과한 최소거리로 문제를 해결할 수 있었다.
# bfs의 visited 업데이트가 정말 복잡한 형태로 되어있고, 벽을 부수고 지나갈때를 처리하는게 너무 어려웠는데 3차원 배열의 visited를 생가하지 못했다.
# 더 심화된 bfs,dfs 문제를 잘 풀도록 해야겠다.
# 추가적으로 최단거리에 대한 생각이 들면 거의 bfs를 먼저 생각하는 식으로 문제를 접근하도록 노력해야겠다.

from collections import deque

n,m = map(int,input().split())

arr = []
for i in range(n):
    s = input()
    arr.append(list(s))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 0)) 
    visited[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == '0' and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
                elif arr[nx][ny] == '1' and wall == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    q.append((nx, ny, 1))
    return -1

print(bfs())