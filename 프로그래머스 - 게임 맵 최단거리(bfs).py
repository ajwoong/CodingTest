from collections import deque

def solution(maps):
    start_x, start_y = 0, 0
    end_x, end_y = len(maps)-1, len(maps[0])-1
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    dq = deque()
    dq.append((start_x, start_y, 1))
    visited[start_x][start_y] = 1
    
    while dq:
        x, y, dist = dq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    if nx == end_x and ny == end_y:
                        return dist + 1
                    visited[nx][ny] = dist + 1
                    dq.append((nx, ny, dist + 1))
    return -1