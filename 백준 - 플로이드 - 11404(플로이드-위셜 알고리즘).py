import math

n = int(input())
m = int(input())

board = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())
    board[a][b] = min(board[a][b], c)

for i in range(1,n+1):
    board[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(board[i][j] > board[i][k] + board[k][j]):
                board[i][j] = board[i][k] + board[k][j]


for i in range(1,n+1):
    for j in range(1, n+1):
        if(board[i][j] == math.inf):
            print(0, end= " ")
        else:
            print(board[i][j], end= " ")
    print("")