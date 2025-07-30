# bfs를 응용한 문제이다
# 현재 문자열 상태를 visited로 저장해두고 0을 이동시키는 것이었다.
# 0이 가능한 위치들을 bfs로 계속 이동시키면서 '123456780' 상태를 같은게 있나 확인하고, 방문한 패턴들은 '02315876' 이런형태로
# visited에 set으로 저장한 것이었다. 집중이 잘 안되고, 구현이 안된다. 제대로 다짐해서 해야겠다.

from collections import deque

start = ''
for _ in range(3):
    start += ''.join(input().split())

target = '123456780'

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = set()
dq = deque()
dq.append((start, 0))
visited.add(start)

while dq:
    now, cnt = dq.popleft()
    
    if now == target:
        print(cnt)
        exit()
    
    idx = now.index('0')
    x = idx // 3
    y = idx % 3

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 3 and 0 <= ny < 3:
            nidx = nx * 3 + ny
            lst = list(now)
            lst[idx], lst[nidx] = lst[nidx], lst[idx]
            new_state = ''.join(lst)
            if new_state not in visited:
                visited.add(new_state)
                dq.append((new_state, cnt + 1))

print(-1)