# dp를 활용하는 문제였다
# dp[i+1]에 대한 값, 즉 해당날짜 이후에 아무것도 안하고 넘어가는 날에 대한 업데이트를 for문으로 돌렷었다.
# 하지만 그건 잘못된 방법이었다. 그냥 같은 포문에서 다음날에 대한 Max정보를 업데이트 해주면 되는것이었다.

import sys
input = sys.stdin.readline

n = int(input())
tlist = []
plist = []

for day in range(n):
    t, p = map(int,input().split())
    tlist.append(t)
    plist.append(p)

dp = [ 0 for _ in range(n+1)]

for day, time in enumerate(tlist):
    dp[day+1] = max(dp[day], dp[day+1])

    if(day + time < n+1):
        dp[day+time] = max(dp[day+time], plist[day] + dp[day])

print(dp[-1])