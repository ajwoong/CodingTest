import math

def solution(n):
    
    two_num = n // 2
    ans = 0
    for i in range(0,two_num+1):
        one_num = n - (2*i)
        ans += math.factorial(one_num + i) // (math.factorial(one_num) * math.factorial(i))
    print(ans)

solution(4)