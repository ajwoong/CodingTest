# 이 문제도 그리디 문제로 요격시스템이랑 비슷하다
# 자동차가 지난 마지막 구간 route[1]을 기준으로 정렬을하고, route[0]이 앞선 자동차의 범위에 있으면 Pass, 없다면 새로운 카메라를 추가한다
# 이런 방식은 유명하니 외우는게 좋겠다.

def solution(routes):
    
    routes.sort(key = lambda x:x[1])
    
    comp = -30000
    answer = 0
    for route in routes:
        if(comp < route[0]):
            comp = route[1]
            answer += 1
        else:
            continue
            
    return answer