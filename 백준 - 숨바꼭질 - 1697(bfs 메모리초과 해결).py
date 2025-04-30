# bfs로 해결하는 문제, 메모리 초과가 나서 조금 어려웠다.
# 여기서 메모리 초과는 visited로 이미 최소거리로 방문한 숫자에 대한 재방문은 하지 않도록 업데이트를 해나가는 bfs였다
# 앞으로 메모리 초과가 안나게 visited로 재방문을 막는것을 꼭해야겠다.

from collections import deque

n,k = map(int,input().split())

q = deque()
q.append(n)
visited = set()
visited.add(n)

cnt = -1
a= -1

while q:
    cnt+=1
    for i in range(len(q)):
        a= q.popleft()
        if(a == k):
            break
        for next_a in (a - 1, a + 1, a * 2):
            if 0 <= next_a <= 100000 and next_a not in visited:
                q.append(next_a)
                visited.add(next_a)
    if(a==k):
        break
    
print(cnt)