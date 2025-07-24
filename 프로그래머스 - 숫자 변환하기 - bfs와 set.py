# 이 문제는 bfs를 활용하되, visited를 set으로 만들어서 방문 탐색여부를 O(1)로 만들어주는 방법이다
# visited를 배열로 했을경우 안에 요소를 확인하기 위해서 O(n)이 연산 속도로 들지만, set은 O(1)만 걸리기때문에 
# visited를 set으로 만들어서 방문여부를 갱신하는 것이다. 이 점을 꼭 기억하자

from collections import deque

def solution(x, y, n):
    
    q= deque()
    q.append((x,0))
    visited = set()
    
    while q:
        a, cnt = q.popleft()
        if(a==y):
            return cnt
        if(a>y or a in visited):
            continue
        visited.add(a)
        q.append((a*2,cnt+1))
        q.append((a*3,cnt+1))
        q.append((a+n, cnt+1))
    
    return -1
        
        
        
    
        
    