# 이 문제는 시간복잡도를 줄이는게 관건이었다
# 하다보니 최대값을 구하고 1을 줄이고 그리고 또 최대값을 구하고 1을 줄이고 하는 방식으로 구현하는 것을 알았다
# 어떤 배열에서 쉽게 최대, 최소값을 구하려면 heapq를 사용할 수 있다
# heapq를 pop하면 최소값이 나온다 
# 따라서 음수로 바꿔줄수 있다

import heapq

def solution(n, works):
    
    if(n>=sum(works)):
        return 0
    
    works = [ w * (-1) for w in works]
    heapq.heapify(works)

    while n>0:
        maxWork = heapq.heappop(works)
        maxWork += 1
        heapq.heappush(works, maxWork)
        n -= 1 

    

    # 내가 heapq 없이 짠 부분:

    # while True:
    #     works.sort(reverse=True)
    #     while(works[0] >= works[1] and n>0):
    #         works[0] = works[0] - 1
    #         n = n - 1
    #     if(n<=0):
    #         break
    
    
    answer = 0
    for x in works:
        answer += x**2
    
    return answer
    