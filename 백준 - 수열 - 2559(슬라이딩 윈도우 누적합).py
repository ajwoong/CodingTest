from collections import deque

n, k = map(int, input().split())
nlist = list(map(int, input().split()))

now_max = sum(nlist[:k])
current_max = now_max
q = deque(nlist[:k])

for i in range(k,n):
    p = q.popleft()
    q.append(nlist[i])
    now_max = now_max - p+nlist[i]
    current_max = max(current_max, now_max)


print(current_max)