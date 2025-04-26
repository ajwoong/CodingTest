# 그래프 탐색 문제인 것도 알게 됐고, bfs를 활용하는 것도 알았다.
# 인접 노드를 queue를 통해서 업데이트 하는 방식을 꼭 외워야겠다.
# 목적지에서부터 인접 노드를 최소한의 루트로 가는 수를 게산해서 구해나가는 방식이다.
# 나는 너무 부족하고 못한다. 그래프 탐색 문제 구현도 못하는거 보니 정말 열심히 해야겠다.
# 우선 모두 distance를 -1로 업데이트해서 도달할 수 없다고 하고, 목적지를 0으로 표시한뒤 딕셔너링서 인접 노드들을 -1 이라면 거리를 계속 + 1 해서 업데이트 하는 방식이다.


from collections import deque, defaultdict

def solution(n,roads, sources, destination):
    dictp = defaultdict(list)

    for i in roads:
        dictp[i[0]].append(i[1])
        dictp[i[1]].append(i[0])
    
    distances = [-1] * (n+1) 

    queue = deque([destination])
    distances[destination] = 0

    while queue:
        now = queue.popleft()
        for neighbor in dictp[now]:
            if (distances[neighbor] == -1):  
                distances[neighbor] = distances[now] + 1
                queue.append(neighbor)
    
    result = [distances[source] for source in sources]
    return result
    