from collections import deque

n, m = map(int,input().split())

board = []
for i in range(n):
    r= list(input())
    board.append(r)

visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
q.append((0,0))
visited[0][0] = 1

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(nx>=0 and ny>=0 and nx < n and ny <m):
            if(board[nx][ny] == '1' and visited[nx][ny] == 0):
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[n-1][m-1])
