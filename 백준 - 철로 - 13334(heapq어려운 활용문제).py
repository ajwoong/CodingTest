# 이 문제는 다른 선분들과 최대한 겹치는 d길이의 선분을 어떻게 배치하는가에 대한 질문이다.
# 이 문제는 우선, 선분들을 모두 오른쪽 끝점을 기준으로 정렬시켜야 한다. 그 이유는 끝점을 고정해, 끝점부터 끝점 - d(철로의 길이)만큼 했을때
# 이 범위 안에 시작점이 있으면 그 선분은 포함시켜야 되기 때문이다.
# 그래서 끝점 기준으로 정렬후, 이후 들어오는 선분들에 대해서 end-d를 확인하고, 그 안에 지금 현재 heapq에 있는 선분들중에 시작점이 최소인, 즉 멀리있는 애들
# 부터 확인해서 구간안에있는지 확인해 구간안에 들어오는 선분개수의 최대를 구하게 하는 것이다.

import heapq

n = int(input())

ways = []
for i in range(n):
    h,o = map(int,input().split())
    start, end = sorted((h,o))
    ways.append((start,end))

d = int(input())
ways.sort(key=lambda x : x[1])

hq = []
answer = 0

for h, o in ways:
    heapq.heappush(hq, h)
    while hq and hq[0] < o - d:
        heapq.heappop(hq)
    answer = max(answer, len(hq))

print(answer)