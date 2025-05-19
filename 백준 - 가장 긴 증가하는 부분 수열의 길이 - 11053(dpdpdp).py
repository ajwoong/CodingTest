# 이번 dp는 아이디어 접근을 이중포문으로만 해도 되는걸 자각하지 못했다.
# 생각보다 되게 쉬운문제인데 이중포문이 가능한지 몰라, 구현을 못했다
# 앞으로 문제조건을 잘봐서 디피라고 무조건 이중포문이 안된다고 생각하지 말아야겠다.

n = int(input())
num = list(map(int,input().split()))

dp = [1] * n

for i in range(1,len(num)):
    for j in range(i):
        if(num[j] < num[i]):
            dp[i] = max(dp[i], dp[j] + 1)
    

print(max(dp))