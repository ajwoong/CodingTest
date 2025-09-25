# 완전 이상한 짓을 했다. 기존에 있는 List는 heapqify로 힙구조로 만들고 나서, 처리를 해야되는데
# 그렇게 안했다. []이거처럼 빈 리스트부터 채워나가는건 Heapify를 해줄 필요 없지만, 이미 존재하는 리스트를
# 이제 힙큐처럼 사용하고 싶다면 heapify를 해줘야한다.

import heapq

t = int(input())

for i in range(t):
    k = int(input())
    klist = list(map(int,input().split()))
    answer = 0

    heapq.heapify(klist)

    while len(klist) > 1:
        a = heapq.heappop(klist)
        b = heapq.heappop(klist)
        s = a + b
        answer += s
        heapq.heappush(klist, s)
    
    print(answer)