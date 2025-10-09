# 해당 문제는 재귀형 dfs를 이용해 visited의 오염을 막아야 하는 문제였다.
# 예를들어 (0,0) -> (0,1) -> (1,2) 이렇게 갔는데 (1,1)에서 막혔다하자
# 근데 다음에 (1,0) 에서 (0,1)로도 가는 경로로 최소 경로가 나올 수 있다.
# 그런데 단순 visited와 stack으로 dfs를 구현하면 여기서 (0,1)이 이미 visited 1로 오염되기 때문에
# 재귀를 통해서 진짜 최적 경로가 아닌경우에는 그 visited경로가 오염되지 않게 해야된다.
# 그래서 최적경로 만을 visited에 저장해야 하는 것이었다
# 또한 방향성이 중요했다 dfs탐색할때 오른쪽 위, 오른쪽, 오른쪽 아래의 순서로 나아가야 한다.
# 왜냐하면 윗줄에서 내려오는 파이프가 아래 줄보다 우선적으로 연결되어야 경로들이 서로 겹치지 않고 최대 개수가 나올 수 있기 때문이다.
# 그래서 이문제는 그리디한 사고와 dfs를 합쳐야 풀 수 있는 문제였다
# 매우 까다로운 문제이니 앞으로는 좀 더 깊은 고민을 하고 푸는 것이 좋겠다.


r, c = map(int,input().split())
bmap = []

for i in range(r):
    b = list(input())
    bmap.append(b)


visited = [[0 for _ in range(c)] for _ in range(r)]
dx = [-1,0,1]
dy = [1,1,1]
answer = 0

def dfs(x, y):
    global answer
    visited[x][y] = 1

    if y == c - 1:
        answer += 1
        return True

    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and bmap[nx][ny] == '.':
                if dfs(nx, ny):
                    return True
    return False

for i in range(r):
    if bmap[i][0] == '.':
        dfs(i, 0)

print(answer)

