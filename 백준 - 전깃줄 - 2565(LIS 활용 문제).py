# 이전에 푼 가장 긴 증가하는 부분 수열의 길이 (LIS) 문제의 활용이다.
# 사실 아이디어를 이전에 푼거였기 때문에, 까먹으면 안되는 문제인데 까먹어서 애를 많이 썼다.
# 이중 포문을 활용하여 배열에서 현재 지점까지의 가장 긴 증가하는 부분 수열의 최대 길이를 업데이트 해나가는 과정이다.
# 예를들어 10, 20, 10, 30 이런배열이있다면
# dp배열을 처음 1로 모두 초기화했을때 마지막 30에서는 30은 10보다 크고 20보다도 크기때문에 dp[10] dp[20]을 볼거고
# 그중에서 최대인 거에다가 +1 하던지 아니면 현재 값이 최대인지를 비교해서 답을 구하는 방식이다.
# 앞으로도 LIS 개념을 절대 절대 까먹지 말아야겠다.

n = int(input())
nlist = []

for i in range(n):
    x, y = map(int,input().split())
    nlist.append([x,y])

nlist.sort()
dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if(nlist[j][0] <= nlist[i][0] and nlist[j][1] <= nlist[i][1]):
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))