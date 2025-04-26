# dp를 활용하는 문제이다.
# dfs로 문제를 풀었는데 시간초과가 나서 dp로 풀어야함을 깨달았다.
# 물 웅덩이를 만나면 거기로 모였던 경우의 수는 0으로 초기화하고, 만나지 않는 지점은 도착하는데 경우의수를 +1을 해준다
# 그렇게 dp라는 배열을 계속 업데이트 해나가며 푸는 문제이다.
# dp 푸는 방법을 잘 익혀야겠다.
# 생각해보면 이문제는 손으로 길찾기 문제를 수학문제처럼 풀었던거랑 완전히 같은 방식이다.

def solution(m, n, puddles):
    
    for puddle in puddles:
        puddle[0] -= 1
        puddle[1] -= 1
    
    dp = [[0] * m for _ in range(n)]
    
    dp[0][0] = 1
    
    for x in range(n):
        for y in range(m):
            if([y,x] in puddles):
                dp[x][y] = 0
            else:
                if(x>0):
                    dp[x][y] += dp[x-1][y]
                if(y>0):
                    dp[x][y] += dp[x][y-1]
                    
    
    return dp[n-1][m-1] % 1000000007
                