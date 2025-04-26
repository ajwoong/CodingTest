# 이분탐색을 활용하여 최소 1 부터 최대 diffs의 최대값까지 배열을 탐색하여 숙련도 최소값을 구하는 문제
# 이분탐색을 직접 구현할 수 있도록 공부해야겠다.
# 전체 배열의 중간값을 항상 Level로 하여서 계속 level값을 업데이트 해나간다.
# 그래서 해당 level이 최소가 되는 값을 구하는 것.

import math 

def solution(diffs, times, limit):
    max_level = max(diffs) 
    l = 1
    r = max_level
    answer = max_level 

    while l < r:
        level = int((l+r) / 2)
        totalTime = times[0]

        for x in range(1, len(diffs)):
            num = 0
            if(level < diffs[x]):
                num = (diffs[x] - level)
            totalTime += (times[x] + times[x-1]) * num +  times[x]
        
        if totalTime <= limit:
            r = level
            answer = level

        else:
            l = level + 1
    
    return answer
        
    