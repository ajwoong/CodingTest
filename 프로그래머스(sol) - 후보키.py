# 후보키의 개념을 몰라서 구현을 제대로 못한 문제이다
# 우선 조합으로 후보키 후보들을 저장한 이후에, 최소성 검사를 진행하는 방향으로 고쳤다
# 최소한으로 조합하여 나온것들 이후에 들어오는 것들은 issubset으로 겹치는 부분이 있다면 못 가져오게 하였다
# 예를들어 (1,2)와 (1,2,3) 을 비교했을때 (1,2)는 (1,2,3)에 포함되므로 이 부분을 issubset함수를 통해서 해결하엿다

from itertools import combinations

# relation = [['a',"1",'aaa','c','ng'],['b',"1",'bbb','c','g'],['c',"1",'aaa','d','ng'],['d',"2",'bbb','d','ng']]
# relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
relation = [["100", "ryan", "music", "2", "O"], ["200", "apeach", "math", "2", "AB"], ["300", "tube", "computer", "3", "AB"], ["400", "con", "computer", "4", "A"], ["500", "muzi", "music", "3", "B"], ["600", "apeach", "music", "2", "O"]]

notUnique = []
kSet = []
answer = 0

for y in range(len(relation[0])):
    relationList = []
    for x in range(len(relation)):
        relationList.append(relation[x][y])
    relationSet = set(relationList)
    if(len(relationSet) != len(relationList)):
        notUnique.append(y)
    else:
        answer += 1 

 
while(len(notUnique) > 1):
    limit = len(notUnique)
    for num in range(2, limit + 1):
        c = combinations(notUnique, num)
        for k in c:
            relationList = []
            for m in range(len(relation)):
                example = ""
                for p in k:
                    example = example + relation[m][p]
                relationList.append(example)
            relationSet = set(relationList)
            if(len(relationSet) == len(relationList)):
                isMinimal = True
                for existing in kSet:
                    if set(existing).issubset(set(k)):
                        isMinimal = False
                        break
                if isMinimal:
                    answer += 1
                    kSet.append(k)
                    
    if(num == limit):
        break

print(kSet)
print(answer)