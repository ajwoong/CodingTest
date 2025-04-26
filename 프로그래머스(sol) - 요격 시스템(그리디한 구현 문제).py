# 접근방법이 중요한 문제였다.
# 미사일의 마지막 개구간을 기준으로 정렬하고, 다른 미사일의 시작 구간이 미사일의 마지막 구간과 겹치는지를 보고 해결할 수 있는 문제였다.

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

newTargets = sorted(targets, key= lambda x : x[1])

gun = 0
answer = 0
for x in range(len(newTargets)):
    if(gun > newTargets[x][0]):
        continue
    gun = newTargets[x][1]
    answer += 1

print(answer)