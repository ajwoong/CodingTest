# dp를 조금더 활용하는 문제였다.
# +,-,안쓰기 3가지의 경우를 통해서 i번째 추를 + - 아예안쓰기로 업데이트해나가는 문제이다
# 아이디어를 잘 탐색했고, 구현으로 이어지는 부분이 조금 어색했지만 잘 하도록 노력해야겠다.

c = int(input())
clist = list(map(int, input().split()))
p = int(input())
plist = list(map(int,input().split()))

dp = [[0 for _ in range(15001)] for _ in range(c)]

dp[0][0] = 1
dp[0][clist[0]] = 1

for i in range(1, c):
    for j in range(15001):
        if dp[i-1][j]:  
            dp[i][j] = 1
            if j + clist[i] <= 15000:
                dp[i][j + clist[i]] = 1
            if abs(j - clist[i]) <= 15000:
                dp[i][abs(j - clist[i])] = 1


answer = ""
for k in plist:
    if k > 15000:
        answer += "N "
    elif dp[c-1][k]:
        answer += "Y "
    else:
        answer += "N "
print(answer)
