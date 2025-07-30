# 교집합으로 해결하는 거 까지 생각함, 이후 구현에서 combination를 통해 교집합 보다 길이가 작은것도
# 공통 메뉴로 나올수가 있다는 사실을 망각함
# 그래서 combinations로 해당 set에서 가능 한 교집합들을 또 전부구해서 result에 저장
# 이후 가장 많이 나온 메뉴를 count를 통해 세줌, 그래서 메뉴구성에서 가장 많이 나온 메뉴만 나올 수 있게함

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    orders_set = []
    for o in orders:
        orders_set.append(set(o))

    result = set()
    for i in range(len(orders_set)):
        for j in range(i+1, len(orders_set)):
            inter = orders_set[i] & orders_set[j]
            for c in course:
                if len(inter) >= c:
                    for comb in combinations(inter, c):
                        result.add(frozenset(comb))

    counter = defaultdict(int)
    for comb in result:
        for o in orders_set:
            if comb.issubset(o):
                counter[comb] += 1

    filtered = []
    for c in course:
        max_count = 0
        for comb, cnt in counter.items():
            if len(comb) == c and cnt >= 2:
                max_count = max(max_count, cnt)
        for comb, cnt in counter.items():
            if len(comb) == c and cnt == max_count:
                filtered.append(''.join(sorted(comb)))

    return sorted(filtered)