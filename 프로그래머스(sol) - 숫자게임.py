# A와 B를 정렬하고 최댓값끼리 비교를 한다. B의 최대값이 A의 최대값보다 크다면 해당 A에 B를 배치하여 점수를 딴다
# 만약 점수를 따지 못할거 같으면, B의 최대값이 A의 최대값보다 작다면, B의 최소값으로 A의 최대값에 배치해 제일 작은걸 소모한다

from collections import deque

def solution(A, B):
    
    A.sort()
    B.sort()
    
    A = deque(A)
    B = deque(B)
    
    answer = 0
    while A and B:
        if(B[-1] > A[-1]):
            A.pop()
            B.pop()
            answer += 1
        else:
            A.pop()
            B.popleft()
    
    return answer