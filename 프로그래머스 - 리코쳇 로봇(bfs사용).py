# 오랜만에 풀어서 조건문, 반복문 조건이 조금 까다로웠다.
# bfs 아이디어는 잘 생각해내서, bfs 구현까지 성공해서 맞았다.
# 더 어려운 문제들을 위주로 풀어보고 고민해봐야겠다.

from collections import deque

def solution(board):
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            if(board[x][y] == 'R'):
                r_point = [x,y]
    
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[r_point[0]][r_point[1]] = 1
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def bfs():
        
        q = deque()
        q.append(r_point)
        cnt = 0
        
        while q:
            point = q.popleft()
            x = point[0]
            y = point[1]
            
            for i in range(4):
                nx = x
                ny = y
                while (0 <= nx + dx[i] < len(board) and 0 <= ny + dy[i] < len(board[0]) and 
                       board[nx + dx[i]][ny + dy[i]] != 'D'):
                    nx += dx[i]
                    ny += dy[i]
                    
                if(visited[nx][ny] == 0 and board[nx][ny] != 'G'):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                elif(visited[nx][ny] == 0 and board[nx][ny] == 'G'):
                    visited[nx][ny] = visited[x][y]
                    return visited[nx][ny]
                
        return -1
    
    answer = bfs()
    return (answer)
                    
                    