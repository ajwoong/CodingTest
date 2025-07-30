# 몇번의 도전 끝에 풀어낸 bfs활용 문제다
# 현재 지점까지 갈수있는 최소 비용 상태를 저장하고, 갱신해나가는 bfs문제였다.

import math
from collections import deque

def solution(board):
    max_x = len(board)
    max_y = len(board[0])
    visited = [[math.inf] * max_y for _ in range(max_x)]
    
    dq = deque()
    dq.append((max_x-1,max_x-1,0,0,-1))
    visited[max_x-1][max_x-1] = 0
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while dq:
        x,y, corner,straight, before_i = dq.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            new_corner, new_straight = corner,straight
            if(0<=nx<max_x and 0<=ny<max_y):
                if(before_i == -1):
                    new_straight += 1
                else:
                    if(before_i != i):
                        new_corner += 1
                        new_straight += 1
                    else:
                        new_straight += 1
                
                new_cost = new_corner*500 + new_straight*100
                if(new_cost <= visited[nx][ny] and board[nx][ny] == 0):
                    visited[nx][ny] = new_cost
                    dq.append((nx,ny,new_corner,new_straight, i))
                    
    return(visited[0][0])
        