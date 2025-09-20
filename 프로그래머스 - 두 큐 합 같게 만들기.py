# 처음에 bfs 방식으로 풀려다 배열을 계속해서 큐에 넣고 이걸 빼서 처리하는 작업을 반복하니 시간복잡도가 올라갈수밖에 없었다
# 이후, 그냥 수가 커질때마다 커진 배열에서 빼서 작은 배열에 넣기를 반복하면 되는 문제임을 깨달았다.

from collections import deque
def solution(queue1, queue2):
    dq1, dq2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(dq1), sum(dq2)
    total = sum1 + sum2
    
    if(total % 2 != 0):
        return -1
    
    target = total // 2
    count = 0
    max_count = len(dq1) * 3
    
    while count <= max_count:
        if(sum1 == target):
            return count
        if(sum1 > target):
            i = dq1.popleft()
            dq2.append(i)
            count += 1
            sum1 -= i
            sum2 += i
        elif(sum2 > target):
            i = dq2.popleft()
            dq1.append(i)
            count += 1
            sum1 += i
            sum2 -= i
            
    return -1