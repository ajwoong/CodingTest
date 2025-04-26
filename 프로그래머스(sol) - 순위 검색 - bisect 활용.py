# 효율성을 높이기 위한 방법들이 있었음
# dictionary를 활용해서 query -> info 검색이 아닌 info에 포함될만한 query를 다 만들어서 딕셔너리로 만든 다음에 query로 딕셔너리를 찾아서 해당 검색이 된 사람들을 찾고, 점수들만 비교하게 만듦
# 점수 비교를 진행할때는 해당 점수 이상인거 리스트에서 전부 찾기 위해 정렬 후 이진 탐색을 bisect라는 걸 이용해 처리
# bisect_left(list, n)-> list에서 n 이상인 원소가 처음 나오는 index 알려줌
# bisect_right(list, n) -> list에서 n 초과인 원소가 처음 나오는 indexd 알려줌

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


people = []
queryList = []
answer = []


for x in info:
    xList = x.split()
    people.append(xList)

dic = defaultdict(list)

for person in people:
    for i in range(5):
        case = combinations([0,1,2,3], i)
        for c in case:
            tmp = person.copy()
            tmp.pop()
            for idx in c:
                tmp[idx] = '-'
            key = ''.join(tmp)
            dic[key].append(int(person[4]))

for value in dic.values():
        value.sort()   


for x in query:
    x = x.replace("and ", "")
    x = x.split()
    newQuery = "".join(x[:-1])
    score = int(x[-1])
    count = 0
    if newQuery in dic:
        targetList = dic[newQuery]
        idx = bisect_left(targetList, score)
        count = len(targetList) - idx
    answer.append(count) 

print(answer)


# searchList = []

# for oneQuery in queryList:
#     searchNum = 0
#     for i in range(len(people)):
#         if(((people[i][0] == oneQuery[0]) or oneQuery[0] == '-') and 
#            ((people[i][1] == oneQuery[1]) or oneQuery[1] == '-') and
#            ((people[i][2] == oneQuery[2]) or oneQuery[2] == '-') and
#            ((people[i][3] == oneQuery[3]) or oneQuery[3] == '-') and
#            (int(people[i][4]) >= int(oneQuery[4]))):
#             searchNum+=1
#     searchList.append(searchNum)

# print(searchList)