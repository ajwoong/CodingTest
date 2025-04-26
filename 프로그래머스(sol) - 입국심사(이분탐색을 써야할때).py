# 이 문제는 주어진 n이 10억이기 때문에, n을 이용해서 배열에 추가하고, sort를 한다면 시간초과가 발생한다.
# 그래서 이분탐색을 활용해야 한다.
# 이분탐색 문제는 처음이라, 어떻게 이분탐색을 적용해야 할지 분간이 안갔다. 여기서는 최소 1초 최대 times에서 주어진 시간 * 사람수가 최대 시간이었다.
# 이를 해결하기 위해서 최소 최대를 잡고 이분탐색을 통해 최적의 시간을 구하는 것이었다.
# 해당 시간을 구해가며 해당 시간에 사람이 최소 n명 만큼 참가할 수 있는지 확인하기를 반복하며 time을 찾는 과정이었다.
# 이분탐색 문제가 나와도 당황하지 않고 제대로 해야겠다. 너무 해이한 정신상태로 문제를 푼 것 같다. 더 독하게 파고들자.
# bisect를 계속 사용하려고 했는데, 이 문제는 어떤 값 이상인 지점을 찾는 문제가 전혀 아니었는데 계속 편하게 하려고 했다.
# 무조건 문제의 조건을 보고 어떤걸 적용할지 생각하며 문제를 풀자.


def solution(n, times):
    
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
            if(people >= n):
                break
                
        if(people >= n):
            answer = mid
            right = mid - 1
        
        else:
            left = mid + 1
        
    return answer
        
        
    
    
        
    