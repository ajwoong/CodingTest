# kruskal 알고리즘과 prim 알고리즘에 대해서 배웠다. 그리디를 구현할때 간선의 최소비용이 되게 선택하는 알고리즘이다
# kruskal 알고리즘은 간선을 최소비용으로 정렬 후, 최소비용이 되는 애들을 선택하면서, cycle이 발생하는지 체크 후, 통과하면 간선으로 추가하는 방식이다.
# prim 알고리즘은 간선을 최소비용으로 정렬 후, 현재 간선으로 연결된 지점에서 확장할 수 있는 애들만 선택해, cycle이 발생하지 않도록 하면서 간선을 추가하는 방식이다.
# 그리디 알고리즘에 자주 사용되는 애들이라고 하니, 외워 두자.


# prim으로 푼거
def solution_prim(n, costs):
    
    ans = 0
    costs = sorted(costs, key=lambda x:x[2])
    visited = set()
    visited.add(costs[0][0])
    
    while(len(visited) != n):
        for i in costs:
            if(i[0] in visited and i[1]  in visited):
                continue
            if(i[0] in visited or i[1] in visited):
                visited.update([i[0], i[1]])
                ans += i[2]
                break   
    
    return ans
            

# kruskal로 푼거
# kruskal 구현방식은 부모 노드를 체크하는 식으로 한다.
# 두 노드를 union한다는 것은, 두 노드의 부모노드를 체크하는것이다. 두 노드의 부모노드가 같다면, 두 노드를 잇게 된다면 cycle이 생기는 것이기 때문에
# 이를 피하기 위해서 그런 과정을 거치는 것이다.
def solution_kruskal(n, costs):
    
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            return False  
        parent[root_b] = root_a
        return True

    costs.sort(key=lambda x: x[2])
    answer = 0

    for a, b, cost in costs:
        if union(a, b): 
            answer += cost  
    return answer