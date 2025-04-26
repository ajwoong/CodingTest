# 또 dp다
# 이번문제는 한 수열에서 연속된 i개의 합이 최대인 값을 구하는 것이었다.
# dp[i]는 i번째 원소까지 봤을때 i를 끝으로 하는 연속합중에서 최대값이다.
# 이러면 점화식이 dp[i] = max(num[i], dp[i-1] + num[i])가 된다.
# 이유는 i까지 선택한 값중에서 i번째 자체가 최대값일 수도 있고, 아니면 이전 dp[i-1] i-1번을 끝으로 하는 연속합중 최대값에서
# 지금 i번째를 더한거가 되기 때문이다.
# dp는 정말 아이디어 싸움인거 같다. 더 잘해지기 위해 노력해야겠다.

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = num[0]

for i in range(1, n):
    dp[i] = max(num[i], dp[i-1] + num[i])

print(dp)
print(max(dp))