# 플로이드-위셜 알고리즘을 활용하여 사이클 최소값을 찾는 문제이다
# i,j는 여기서 i에서 출발해 j까지 가는 최소 거리를 의미한다. 
# 그래서 i,j는 i,k k,j로 표현할수 있고 이말은 i에서 j까지의 거리는 i에서 k까지가는 최소거리 + k에서 j까지 가는 최소거리이다.
# 여기서 3중 for문을 작성할때 k를 제일먼저 한것은 i에서j까지 가는것이 기본이고 k가 중간거처인데, 이 중간 거처를 제일 큰 for문으로 돌려야
# 업데이트가 되는데 적합해서 이다.
# 새로운 알고리즘인 플로이드-위셜 알고리즘을 배웠다. 프림과 크루수칼 알고리즘이 생각났는데, 이건 사이클을 안만드는 최소경로였다.
# 알고리즘들이 헷갈리지 않게 정확히 공부하고 익혀야겠다.

import sys
input = sys.stdin.readline
import math

v, e = map(int,input().split())

board = [[math.inf for _ in range(v+1)] for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    board[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

ans = math.inf
for i in range(1,v+1):
    ans = min(ans, board[i][i])

if(ans==math.inf):
    print(-1)
else:
    print(ans)