import math 

def solution(k, d):
    
    cnt = 0    
    for a in range(0,d+1,k):
        bmax = math.sqrt((d ** 2) - (a) ** (2))
        cnt += bmax//k + 1
    
    return(cnt)