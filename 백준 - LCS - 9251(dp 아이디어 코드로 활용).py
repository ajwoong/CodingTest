# 아이디어는 생각할 수 있었지만, max값을 찾는과정을 while문을 통해서 해서 시간초과가 났다.
# 아이디어는 다음과 같다. 문자열 m과 문자열 n이 있다고 했을 때,
# 문자열 m의 문자를 앞에서부터 하나씩 가져와 문자열 n 전체와 비교한다.
# 이때 만약 해당 문자를 문자열 n에서 찾으면, 그 문자열 전 중에서 dp의 최대값을 찾아 + 1을 해 dp를 갱신한다.
# dp 배열이 의미하는 것은, 해당 문자열로 끝나는 공통 문자열의 길이중에서 최대가 되는 것이다.

m = list(input())
n = list(input())

dp = [0 for _ in range(len(m))]

for i in range(len(m)):
    for j in range(len(n)-1,-1,-1):
        if(n[j] == m[i]):
            cnt = j
            max_cnt = 0
            if(cnt > 0):
                while(cnt > 0):
                    cnt -= 1
                    max_cnt = max(max_cnt, dp[cnt])
                dp[j] = max_cnt + 1
            else:
                if(dp[j] == 0):
                    dp[j] += 1



m = list(input().strip())
n = list(input().strip())

dp = [0] * len(n)

for i in range(len(m)):
    prev_dp = dp[:]  
    max_cnt = 0       
    for j in range(len(n)):  
        if m[i] == n[j]:
            dp[j] = max_cnt + 1
        max_cnt = max(max_cnt, prev_dp[j])  

print(max(dp))