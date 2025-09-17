# 스택과 큐를 활용해 해결하였다.
# 스택에 큐에서 먼저 빠져나가야하는 인덱스값을 저장하는 방식을 사용하였다.

def solution(priorities, location):
    max_p = max(priorities)
    max_p_index = priorities.index(max_p)
    priorities[max_p_index] = 0
    
    stack = []
    stack.append(max_p_index)
    
    while True:
        new_max_p = max(priorities)
        if(new_max_p == 0):
            break
        
        for i in range(stack[-1],len(priorities),1):
            if(priorities[i] == new_max_p):
                priorities[i] = 0
                stack.append(i)
        for j in range(stack[-1]+1):
            if(priorities[j] == new_max_p):
                priorities[j] = 0
                stack.append(j)
    
    return(stack.index(location) + 1)
                