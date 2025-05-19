# 헷갈렸던 점 -> heapify를 언제 사용하는 것인가
# heappush로 list에 넣으면 Heap구조가 지켜지기 때문에, heapfiy를 할필요가 없다.
# 그런데 그냥 일반 리스트에서 heappop을 해도 최소값 출력이 안될 수 있다.
# 그래서 우리는 주어진 리스트의 최소값을 힙으로 pop하고 싶다면, Heapify를 해주고 heappop을 해주어야 한다.

import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []

for i in range(n):
    x = int(input())

    if(x==0):
        if(hq):
            k = heapq.heappop(hq)
            print(k)
        else:
            print(0)
    
    else:
        heapq.heappush(hq, x)