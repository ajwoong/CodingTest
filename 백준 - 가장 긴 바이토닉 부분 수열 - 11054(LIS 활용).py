# LIS 문제를 응용한 또다른 문제이다.
# 가장 긴 부분 바이토닉 수열을 구하는 문제인데, 잘 살펴보면 앞에서부터 LIS 뒤에서부터 LIS의 길이를 더하는 문제이다.

n = int(input())

nlist = list(map(int,input().split()))


dp1 = [1] * n
dp2 = [0] * n

for i in range(1,n):
    for j in range(i):
        if(nlist[i] > nlist[j]):
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-2,-1,-1):
    for j in range(i,n):
        if(nlist[i] > nlist[j]):
            dp2[i] = max(dp2[i], dp2[j]+1)


answer = []

for i in range(n):
    answer.append(dp1[i] + dp2[i])


print(max(answer))