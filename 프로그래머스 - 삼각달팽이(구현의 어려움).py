# 이 문제는 방문 방식에 대한 생각은 했는데, 구현과정에서 머릿속에 있는것을 코드로 만드는 부분이 부족했다.
# 앞으로 더 많은 문제를 접하며 코드로 풀어내는 능력을 길러야겠다.

def solution(n):
    array   = []
    visited = []
    for i in range(n):
        array.append( [0] * (i+1) )
        visited.append([0] * (i+1))    

    dx = [1, 0, -1]
    dy = [0, 1, -1]

    x = 0
    y = 0
    visited[0][0] = 1
    array[0][0]   = 1
    step = 2
    direction = 0  

    total = n*(n+1)//2

    while step <= total:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if not (0 <= nx < n and 0 <= ny <= nx and visited[nx][ny] == 0):
            direction = (direction + 1) % 3
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny
        visited[x][y] = 1
        array[x][y]   = step
        step += 1
    
    answer = []
    
    for i in range(n):
        for j in range(len(array[i])):
            answer.append(array[i][j])
    
    return(answer)