# 다익스트라 알고리즘을 활용하는 문제가 나왔다.
# 최단경로를 생각했을때 플로이드-위셜 알고리즘만 떠올랐는데 한 노드에서만을 기준으로 다른 노드로 가는 최단거리를 구할때는 더 작은 시간복잡도로
# 다익스트라 알고리즘을 선택할 수 있다는 것을 알았다.
# 다익스트라 알고리즘은 한 노드에서 다른 노드로 뻗어나가는 것의 최단 시간을 구하면서 힙큐로 계속 이어서 나오는 노드로의
# 최단 거리를 더해서 최단거리를 업데이트해나가는 방식을 의미한다


import sys
import math
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

dist = [math.inf] * (v+1)
dist[start] = 0

hq = [(0, start)]

while hq:
    cost, now = heapq.heappop(hq)
    if dist[now] < cost:
        continue
    for next_node, weight in graph[now]:
        new_cost = cost + weight
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(hq, (new_cost, next_node))

for i in range(1, v+1):
    if dist[i] == math.inf:
        print("INF")
    else:
        print(dist[i])