# bfs를 사용해 방이 나누어진 영역을 찾고, 이후 방간의 인접한 방들중에서 영역을 합쳤을때 크기가 제일 커지는 경우까지 구하는 방식이었다.
# bfs, dfs에 대한 감을 확실히 익힐 수 있는 문제였다.

from collections import deque

n, m = map(int,input().split())
castle = []

for i in range(m):
    mlist = list(map(int,input().split()))
    bin_mlist = []
    for j in mlist:
        bin_mlist.append(format(j,'b').zfill(4))
    castle.append(bin_mlist)

visited = [[0 for _ in range(n)] for _ in range(m)]
now_visiting = 0
room_size_list = []

for i in range(m):
    for j in range(n):
        room_size = 0
        if(visited[i][j] == 0):
            now_visiting += 1
            room_size += 1
            visited[i][j] = now_visiting
            dq = deque()
            dq.append((i,j))
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]

            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    if(castle[x][y][k] == '0'):
                        mx = x + dx[k]
                        my = y + dy[k]
                        if(0 <= mx < m and 0 <= my < n):
                            if(visited[mx][my] == 0):
                                visited[mx][my] = now_visiting
                                dq.append((mx,my))
                                room_size += 1

            room_size_list.append(room_size)

print(len(room_size_list))
print(max(room_size_list))

expect = set()

for i in range(m):
    for j in range(n):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        point = visited[i][j]
        for k in range(4):
            mx = i + dx[k]
            my = j + dy[k]
            if(0<= mx <m and 0<= my <n):
                if(point != visited[mx][my]):
                    if(point < visited[mx][my]):
                        expect.add((point, visited[mx][my]))
                    else:
                        expect.add((visited[mx][my], point))


maxable_room = max(room_size_list)
for e in expect:
    maxable_room = max(maxable_room, room_size_list[e[0]-1] + room_size_list[e[1]-1])

print(maxable_room)
