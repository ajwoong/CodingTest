# 이 문제는 기지국 개수를 구하는거 까지는 생각이 되었지만, station이 들어올때 빈 구간의 범위를 그리디하게 구하는게 어려웠다
# 처음에 1부터 시작하고 station이 들어오면 그 station의 처음부터 끝까지를 구한 뒤 현재 시작점을 통해 범위를 계속 업데이트 해나가는 방식이었다. 

import math

def solution(n, stations, w):
    
    start = 1
    answer = 0
    for i in stations:
        nend, nstart = i - w, i + w
        if(nend < 1):
            nend = 1
        if(nstart > n):
            nstart = n
        answer += math.ceil((nend-start) / (2*w+1))
        start = nstart + 1
    
    if(n-start >= 0):
        answer += math.ceil((n-start+1) / (2*w+1))
    
    return(answer)
    

             