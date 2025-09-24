# 항상 dfs, bfs문제 풀이에서 기억해야 하는 점은 최단거리에 대해서 물어보는 문제는 bfs를 사용해야 하는 것이다.
# 지금도 케빈베이컨 6단계 법칙으로 아는 사람을 구할때 최소의 경로를 채택해서, 이것이 점수기 때문에 이 문제에서도 bfs를 사용해야한다.

from collections import defaultdict
from collections import deque
import math

n, m = map(int,input().split())
dict = defaultdict(list)

answer = [math.inf for _ in range(n+1)]

for i in range(m):
    f1, f2 = map(int,input().split())
    dict[f1].append(f2)
    dict[f2].append(f1)

for i in range(1, n+1):
    dq = deque()
    visited = [0 for _ in range(n+1)]
    dq.append(i)

    while dq:
        p = dq.popleft()
        
        for friend in dict[p]:
            if(friend != i):
                if(visited[friend] == 0):
                    visited[friend] = visited[p] + 1
                    dq.append(friend)
        
    answer[i] = sum(visited)

print(answer.index(min(answer)))