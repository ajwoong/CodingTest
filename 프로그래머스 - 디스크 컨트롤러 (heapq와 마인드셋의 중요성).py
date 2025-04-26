# heapq를 활용해서 해결하는 문제이다.
# 처음에 무조건 모든 작업을 heapq에 넣어서 결정하려고 했는데, 생각해보니 한 작업을 한 이후에, 다음으로 가능한 작업들을
# heapq에 넣고 거기서 pop하면서 작업을 하고, 그 작업을 하고나서도 심지어, 다음으로 가능한 작업들을 heapq에 넣어주어야 했다.
# 그리고 한 작업이 끝나고 다음 작업에 대한 요청이 중첩되어서 일어나는 것이 아니라, 한 작업이 다 끝나고 요청이 오는 것이면, 
# 현재시간도 그 다음 작업이 마치는 시간으로 조정해야 했다. 
# 여러것들을 고려해서 heapq를 사용해서 구현했어야 하는데, 너무 간단하게 생각했다.
# 오랜만에, 스스로 디버깅을 하고 고쳐보며 코드를 구현했다. 요즘 너무 쉽게 답을 보고, 답을 제출하려 한다.
# 실제 코딩테스트를 보듯이 테스트케이스를 엄청 많이 스스로 생각해보면서 문제를 푸는 습관을 들이자. 나는 무조건 한다.

import heapq, math

def solution(jobs):

    new_jobs = []
    for j_index, j in enumerate(jobs):
        new_jobs.append((j[1], j[0], j_index))
    
    new_jobs = sorted(new_jobs, key=lambda x:x[1], reverse=True)
    start = new_jobs.pop()
    
    hq = []
    heapq.heappush(hq, start)
    
    now = start[1]
    answer = []
    
    while hq:
        i = heapq.heappop(hq)
        now = now + i[0]
        answer.append(now - i[1])
    
    while new_jobs:
        if (new_jobs and (new_jobs[-1][1] <= now)):
            while new_jobs and (new_jobs[-1][1] <= now):
                    a = new_jobs.pop()
                    heapq.heappush(hq, a)
        elif (new_jobs and (new_jobs[-1][1]) > now):
            a = new_jobs.pop()
            heapq.heappush(hq,a)
        
        while hq:
            i = heapq.heappop(hq)
            if(i[1] > now):
                now = i[0] + i[1]
                answer.append(i[0])
            else:
                now = now + i[0]
                answer.append(now - i[1])
                if (new_jobs and (new_jobs[-1][1] <= now)):
                    while new_jobs and (new_jobs[-1][1] <= now):
                            a = new_jobs.pop()
                            heapq.heappush(hq, a)
                
    return math.floor(sum(answer) / len(answer))

