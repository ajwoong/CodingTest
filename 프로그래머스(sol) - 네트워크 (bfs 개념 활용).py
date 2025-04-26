# dfs, bfs를 활용해서 x열에서 (x,y)중에서 (x,y)가 1인 지점의 y를 찾아서 y열로 또 이동하여 열을 전부 방문하는 방식이다.
# 이미 방문한 열은 다시 방문하지 않도록 visited를 사용한다. bfs의 구현은 큐로, dfs의 구현은 스택으로 한다.
# 그렇게 한 열에서의 방문이 전부 끝나서 visited를 전부 업데이트하고 나서 answer를 1늘려주고 이후 다른 열에서 또 bfs를 할 수 있는지 탐색한다. 
# 정말 기초적인 문제인데 못했다. 반성하고 다시 공부 해야겠다.

# dfs를 활용한 풀이는 인접한게 아닌 깊이 우선 탐색이다
# 인접한걸 만날때마다 그 안으로 들어가서 찾는게 dfs라고 보면된다. 
# 네트워크에서 해당 컴퓨터를 찾아가는 과정이라고 보면 되겠다.

# 반성을 정말 많이하고 이 유형이 나올때 공부를 제대로 해서 틀리지말자

from collections import deque

def solution(n, computers):
    
    def bfs(x):
        dq = deque()
        dq.append(x)
        while dq:
            a = dq.popleft()
            visited[a] = 1
            for m in range(n):
                if(computers[a][m] == 1 and visited[m] == 0):
                    dq.append(m)
    
    answer = 0
    visited = [0 for x in range(len(computers))]
    for x in range(n):
        if(visited[x] == 0):
            bfs(x)
            answer += 1
    
    return answer


def solution2(n, computers):
    
    def dfs(x):
        visited[x] = 1
        for k in range(n):
            if(computers[x][k] == 1 and visited[k] == 0):
                dfs(k)
    
    
    answer = 0 
    visited = [0 for _ in range(len(computers))]
    
    for x in range(n):
        if(visited[x] == 0):
            dfs(x)
            answer += 1
    
    return answer