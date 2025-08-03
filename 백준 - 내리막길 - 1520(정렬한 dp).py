# 이 문제는 메모이제이션을 활용한 길찾기 문제 dp였다. 프로그래머스에서 푼 등굣길 문제가 기본원리로 적용된다.
# 그런데 여기서는 내리막길로 이동을 하기 때문에, 무조건 큰수부터 작은수를 방문하고, 그 경로를 저장한다.
# 그래서 먼저 높이를 내림차순으로 정렬한다.
# 맨 처음에 그럼 좌표의 정보가 깨지는 것 아닐까? 했는데 이 정렬은 어짜피 내리막길로만 이동해야하고 내리막으로 돌아서 가는 경로도 
# 추가되는 경우에는 결국에는 해당 지점보다 더 높았던 곳들을 돌아돌아 가야하는 것이기 때문에, 정렬을 해도 상관이없다.
# 즉, 이 dp 길찾기 문제의 핵심은 높이 순으로 정렬을 하고 방문을 하는 것이다. 그렇게 정렬을해도 문제의 조건이 내리막 이동이기 때문에 아무런 영향이 없고,
# 제일 높은 곳에서부터 차근차근 낮아지게 이동할 수 있다.
# 앞으로도 이런 문제가 나오면 정렬을 우선으로 하는건 어떤지 생각해보자.

m, n = map(int,input().split())
board = []

for i in range(m):
    l = list(map(int, input().split())) 
    board.append(l)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

new_board = []
for x in range(m):
    for y in range(n):
        new_board.append((board[x][y], x, y))
new_board.sort(reverse=True)
        

dp =[[0 for _ in range(n)] for _ in range(m)]
dp[0][0] = 1

for element in new_board:
    x = element[1]
    y = element[2]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<m and 0<=ny<n):
            if(board[nx][ny] < board[x][y]):
                dp[nx][ny] += dp[x][y]
print(dp)
print(dp[m-1][n-1])
