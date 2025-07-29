# visited 계산이 많이걸릴거 같다면 set으로 하는것을 잊지말자

a, p = map(int,input().split())

visited = set()
track = []

start = a

while start not in visited:
    visited.add(start)
    track.append(start)
    nsum = 0
    for i in str(start):
        nsum += int(i) ** p
    start = nsum

cnt = 0
for i in range(len(track)):
    if track[i] == start:
        cnt = i
        break

print(cnt)