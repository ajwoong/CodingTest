# 이 문제는 현재 최소값을 기준으로 양 옆 배열들에서 순서를 유지하면서 최소값을 찾아가는 방식이었다
# 예를들어 최소값 왼쪽 배열이 27 65 -16 -2 58 이었으면
# 27,-16 이 최소값 누적이 된다.
# 또한 최소값 오른쪽 배열이 -61 -68 -71 -33 이라면
# -33, -71이 최소값 누적이 된다.
# 아이디어도 떠올랐고 heapq 구현 방식도 생각했지만, 일일이 배열을 heapify하고, heappop하는 방식을 채택하려 했다가
# 시간초과가 났다 순차적으로 heap에다가 집어넣어서 heap[0]로 배열의 누적된 최소값을 가져오는게 더 나은 방식이었다. 

import heapq

def solution(a):

    answer = []
    mina = min(a)
    answer.append(mina)

    first_group = a[0:a.index(mina)]
    last_group =a[a.index(mina)+1:]
    

    heap = []
    for i in range(len(first_group)):
        heapq.heappush(heap, first_group[i])
        answer.append(heap[0])  

    heap = []
    for i in range(len(last_group)-1, -1, -1):
        heapq.heappush(heap, last_group[i])
        answer.append(heap[0])
        

    return len(set(answer))