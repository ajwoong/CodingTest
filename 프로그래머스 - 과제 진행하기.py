# 큐와 스택을 이용한 스케줄링 문제이다
# 흐름을 먼저 손으로 적어서 스케줄링을 천천히 구현하는 문제였다.

from collections import deque

def solution(plans):
    
    plan_list = deque(sorted(plans, key = lambda x:x[1]))
    for i in range(len(plan_list)):
        h, m = plan_list[i][1].split(":")
        plan_list[i][1] = int(h) * 60 + int(m)
        plan_list[i][2] = int(plan_list[i][2])
        plan_list[i].append(plan_list[i][1] + plan_list[i][2])
        
    ready_q = []
    answer = []
    before = plan_list.popleft()
        
    while plan_list:
        now = plan_list.popleft()
        if(before[1] < now[1] < before[3]):
            before[2] = before[2] - (now[1] - before[1])
            ready_q.append([before[0], before[2]])
        elif(before[3] == now[1]):
            answer.append(before[0])
        elif(before[3] < now[1]):
            answer.append(before[0])
            left_time = now[1] - before[3]
            while(left_time != 0 and ready_q):
                if(ready_q[-1][1] > left_time):
                    ready_q[-1][1] -= left_time
                    left_time = 0
                else:
                    left_time -= ready_q[-1][1]
                    answer.append(ready_q[-1][0])
                    ready_q.pop()
        before = now
    
    answer.append(now[0])
    while(ready_q):
        time = ready_q.pop()
        answer.append(time[0])
    
    return answer
                    
        
            
            
        
    