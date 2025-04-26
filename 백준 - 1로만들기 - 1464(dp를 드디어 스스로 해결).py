# 드디어 처음으로 아무것도 안보고 내 힘으로 풀어낸 dp문제이다.
# 모두 top-down으로 풀었지만, 나는 bottom up 방식으로 풀어냈다.
# 나도 할 수 있다는 것을 깨달은 시간이었다.

import math
n = int(input())

dp = [math.inf for _ in range(n+1)]
dp[1] = 0

for i in range(1,n+1):
    if(i*2 <= n):
        dp[i*2] = min(dp[i] + 1, dp[i*2])
    if(i*3 <= n):
        dp[i*3] = min(dp[i] + 1, dp[i * 3])
    if(i+1 <= n):
        dp[i + 1] = min(dp[i] + 1, dp[i + 1])

print(dp[n])