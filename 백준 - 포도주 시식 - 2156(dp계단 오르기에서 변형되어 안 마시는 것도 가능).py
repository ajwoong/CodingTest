# 해당 문제는 이전에 푼 백준 계단 오르기 문제와 상당히 유사하다.
# 다만 계단 오르기 문제에서는 마지막 계단을 밟아야 한다는 점에서 이 문제와 달랐다.
# 이 문제는 해당 계단을 밟지 않고, 이번 포도주를 마시지 않았을때도 최대가 되는 경우가 있기 때문에 이 점을 생각해야 했다.
# dp의 조건을 자세히 읽고, 조건에 따라 dp 점화식을 세우는데 유의해야겠다.

n = int(input())

plist = []
for i in range(n):
    k = int(input())
    plist.append(k)

dp = [0] * (n)
if(n==1):
    dp[0] = plist[0]
elif(n==2):
    dp[0] = plist[0]
    dp[1] = plist[0] + plist[1]
elif(n>=3):
    dp[0] = plist[0]
    dp[1] = plist[0] + plist[1]
    dp[2] = max(dp[1], plist[0]+plist[2], plist[1] + plist[2])
    for i in range(3,n):
        dp[i] = max(dp[i-1], dp[i-2] + plist[i], dp[i-3] + plist[i-1] + plist[i])

print(dp[i])