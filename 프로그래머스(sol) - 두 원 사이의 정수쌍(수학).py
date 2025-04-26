# r2와 r1을 x=i를 기준으로 r2일때가 최대, r1일때가 최소이고 두 점 사이의 정수 점들이 몇개인지 구하는 것이다
# 여기서 x=i가 r1을 넘어서게 된다면 r1값이 아니라 0부터로 해서 두 점사이의 점 개수를 구한다
# 수학적 사고가 굉장히 중요한 문제이다. 이런 문제를 많이 풀어서 수학적 사고를 늘리도록 해야겠다

import math

r1, r2 = map(int, input().split())
answer = 0

for x in range(1,r2+1):
    if(x< r1):
        yStart = math.ceil(math.sqrt((r1**2) - (x**2)))
    else:
        yStart = 0
    yEnd = int(math.sqrt((r2**2 - x**2)))
    answer = answer + yEnd - yStart + 1


answer *= 4

print(answer)