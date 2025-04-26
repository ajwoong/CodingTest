# 이분 탐색 그래프를 찾는 문제였다.
# 이분 탐색 그래프는 인접한 노드를 빨,파 색깔로 번갈아서 색칠했을때, 인접한 노드끼리 같은 색깔이 있다면 이분탐색 그래프가 아니다.
# 해당 방식을 dfs를 활용하여, 구현했다. 구현은 제대로 했지만 그래프에 대한 지식이 많이 부족했다.
# 그래프는 우선 노드끼리 연결이 안되어있을수도 있다. 간선이 존재하지 않을 수도 있다는 뜻이다.
# 그래서 색칠을 할때도 색칠되어있지 않은 노드를 탐색한후, 해당 노드에서 dfs를 돌리는 방식으로 구현해야 했다.

import sys
input = sys.stdin.readline

from collections import defaultdict

k = int(input())

for i in range(k):
    v,e = map(int,input().split())
    vdict = defaultdict(list)
    
    for i in range(e):
        a, b = map(int,input().split())
        vdict[a].append(b)
        vdict[b].append(a)

    color = [-1] * (v+1)

    check = "YES"
    for i in range(1, v+1):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            while stack:
                p = stack.pop()
                for x in vdict[p]:
                    if color[x] == -1:
                        color[x] = 1 - color[p]
                        stack.append(x)
                    elif color[x] == color[p]:
                        check = "NO"
    
    print(check)


