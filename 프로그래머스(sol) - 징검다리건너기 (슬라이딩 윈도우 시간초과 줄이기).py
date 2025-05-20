# 슬라이딩 윈도우를 활용하여 k 구간안에서 최대값을 구하고 그 최대값들 중에서 제일 최소인 값을 구하는게 문제였다
# 다만 슬라이딩 윈도우 특성상 O(kn) 만큼의 시간복잡도가 필요해서 시간초과가 났다. 이부분을 해결하기 위해서 최적화가 필요했다.
# 바로 큐를 활용한 슬라이딩 윈도우이다.
# 큐에서는 1. 슬라이딩 윈도우 범위 밖에 벗어난 친구들은 제거하고, 2. 슬라이딩 윈도우에서 최대값이 가져와진다면, 그것보다 작은 애들은 큐에서 전부 나가리고, 
# 3. 슬라이딩 윈도우 크기만큼 인덱스가 됐다면, 큐[0] 즉 큐의 최대값과 아까 구했던 최대값을 계속 비교하면서 제일 작은거를 꺼내오는 방식이다. 
# 솔직히 다시나오면 구현하기 굉장히 어렵겠지만, 노력해서 구해보도록하자 화이팅!

from collections import deque
import math

def solution(stones, k):
    
    q = deque()
    cmax = math.inf
    for i in range(len(stones)):
        while q and q[0] < i-k+1:
            q.popleft()
        while q and stones[q[-1]] < stones[i]:
            q.pop()
            
        q.append(i)     
        if i >= k - 1:
            cmax = min(cmax, stones[q[0]])
            
    return cmax
    

def mysolution(stones,k):
    qlist = []
    for i in range(len(stones) - k + 1):
        qlist.append(max(stones[i:i+k]))
    return min(qlist)