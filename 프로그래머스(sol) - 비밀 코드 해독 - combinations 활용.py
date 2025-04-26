# 이 문제는 combinations에 대한 이해도가 필요한 문제이다
# combinations(list, n) 하면 list안의 항목들을 활용하여 n개만큼 뽑아서 set을 만들어주고, 중복된거는 제거된다!


from itertools import combinations

n = 10
q = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
ans = [2, 1, 3, 0, 1]
result = 0

candidateList = []
for x in range(1, n+1):
    candidateList.append(x)


codeCandidate = combinations(candidateList, 5)


for oneCandidate in codeCandidate:
    for i in range(len(ans)):
        count = 0
        for x in q[i]:
            if x in oneCandidate:
                count += 1
        if (count != ans[i]):
            break
    else:
        result += 1

print(result)
