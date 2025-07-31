test = int(input())

for i in range(test):
    n = int(input())

    dp = [1 for _ in range(n)]
    for j in range(3, n):
        dp[j] = dp[j-2] + dp [j-3]

    print(dp[n-1])

    

    