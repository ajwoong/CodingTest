# dp를 활용하는 문제이다.
# dp 배열을 통해 가능한 a, b 누적합 상태를 계속 업데이트 하는 것
# 추가적으로 정해진 a_limit과 b_limit 한에서 가능한 info의 명령들을 거르는 방식이다.

info = [[1, 2], [2, 3], [2, 1]]
n = 4
m = 4

dp = [[False for _ in range(m)] for _ in range(n)]
dp[0][0] = True

for a, b in info:
    next_dp = [[False for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if dp[x][y]:
                if x + a < n:
                    next_dp[x + a][y] = True
                if y + b < m:
                    next_dp[x][y+b] = True
    dp = next_dp

minA = float('inf')
for a in range(n):
    for b in range(m):
        if dp[a][b]:
            minA = min(minA, a)

print (minA if minA != float('inf') else -1)