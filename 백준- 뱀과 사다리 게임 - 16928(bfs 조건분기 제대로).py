# 간과한점은 예상 destination을 우선, snake 탄경우, ladder 탄 경우, 정통법으로 간경우로 해서 그 세가지 결과중에서
# 만약 해당 결과점을 방문한적이 없다면 그걸 업데이트 하는 방식으로 문제를 해결하면 되는것이었다.
# 그런데 조건문 분기를 제대로 처리하지 못해서 오류가 발생하였다. 앞으로는 조건문 분기를 제대로 처리하도록 해야겠다.

from collections import deque

n, m = map(int,input().split())

ladder = dict()
snake = dict()

for i in range(n):
    x, y = map(int,input().split())
    ladder[x] = y

for i in range(m):
    x, y = map(int,input().split())
    snake[x] = y

visited = [0 for _ in range(101)]
q = deque()
q.append(1)

while q:
    a = q.popleft()
    for i in range(1,7):
        if(a+i <= 100):
            dest = a + i
            if(a+i in ladder):
                dest = ladder[dest]
            elif(a+i in snake):
                dest = snake[dest]
            if (visited[dest] == 0):
                q.append(dest)
                visited[dest] = visited[a] + 1
    
    if(visited[100] != 0):
        break

print(visited[100])