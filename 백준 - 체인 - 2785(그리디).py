# 그리디 문제였다.
# 체인을 우선 작은 순으로 정렬하고, 길이가 작은 체인부터 고리 한개씩 풀러 큰 2개를 계속해서 이어주는 방식으로 문제를 해결하였다.

from collections import deque
n = int(input())
chain = list(map(int,input().split()))

chain.sort()
chain = deque(chain)

answer = 0

while len(chain) > 1:
    if(chain[0] > 0):
        chain[0] -= 1 
        answer += 1
        new = 0
        for i in range(2):
            if(chain):
                new += chain.pop()
        chain.append(new)
    elif(chain[0] <= 0):
        chain.popleft()

print(answer)