# 정말 많은 시도 끝에 푼 문제
# 각 로봇의 초별 위치를 저장하고 초마다 위치가 겹치는 것들이 충돌 위험이라고 생각하면 되는 문제였다
# Counter는 리스트를 입력받고 해당 리스트에서 각 요소가 몇번 중복되는지 count를 해준다
# Counter는 string을 입력받아도 하나의 string이 몇 번 중독되는지 count가 된다. 

# 여기서 딕셔너리 키를 튜플로 바꾸고 counter에 집어넣어야하는 이유는 딕셔너리의 키는 변할수 없기 때문이다. 그래서 변경가능한 list를 넣을 수가 없다
# 그래서 변경 불가능한 튜플로 변환하고 counter에 집어넣어야 하는 것이다.

from collections import Counter
from copy import deepcopy
from collections import defaultdict

points =[[3, 2], [6, 4], [4, 7], [1, 4]]
routes = 	[[4, 2], [1, 3], [4, 2], [4, 3]]

robot = defaultdict(list)


for route in routes:
    i = 0
    cho = 0
    robotNow = deepcopy(points[route[i] - 1])
    robotDest = deepcopy(points[route[i+1] - 1])
    while(i<=len(routes[0]) - 1):

        robot[cho].append(deepcopy(robotNow))
        if(robotNow[0] != robotDest[0] and robotNow[1] != robotDest[1]):
            if(robotNow[0] > robotDest[0]):
                robotNow[0] -= 1
            else:
                robotNow[0] += 1
        elif(robotNow[0] != robotDest[0] and robotNow[1] == robotDest[1]):
            if(robotNow[0] > robotDest[0]):
                robotNow[0] -= 1
            else:
                robotNow[0] += 1 
        elif(robotNow[0] == robotDest[0] and robotNow[1] != robotDest[1]):
            if(robotNow[1] > robotDest[1]):
                robotNow[1] -= 1
            else:
                robotNow[1] += 1
        
        if(robotNow[0] == robotDest[0] and robotNow[1] == robotDest[1]):
            i += 1
            if(i + 1<= len(routes[0]) - 1):
                robotDest = deepcopy(points[route[i+1] - 1])
        
        cho += 1

answer = 0
for key, values in robot.items():
    counter = Counter(map(tuple, values))
    for x in counter.values():
        if x > 1:
            answer += 1

print(answer)
   
    