# 이번 dp문제는 접근을 하긴 했다
# 해당 계단 위치까지 올라올 수 있는 최대값을 0부터 시작하는 방향으로 잡았다.
# 하지만 계단을 연속 3개를 밟을 수 없다는 조건을 반영하는 dp 배열을 만들기가 쉽지 않았다.
# 조건이 걸려있는 dp도 잘 해결할 수 있도록 해야겠다.

s = int(input())

stair = [int(input()) for _ in range(s)]
dp = [0] * s

if s == 1:
    dp[0] = stair[0]
elif s == 2:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
elif s >= 3:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3, s):
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[s - 1])