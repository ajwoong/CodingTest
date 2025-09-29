# 이 문제는 그리디 문제다
# 우선, 문장의 길이를 제일 길게 늘리는 것이 가장 커질 수 있는 방법이기 때문에, 문장의 길이를 cost내로 가장 길게 만드는 방법을 찾는 것이었다.
# 그 후 가장 긴 번호의 길이를 알아내면, 제일 높은 자리수부터 남은 비용으로 최대 숫자로 바꿀 수 있는지 확인해보며 최대 숫자로 바꾸는 방식이었다.
# 그리디한 사고력을 더욱 기르고, 이를 구현할 수 있을때까지 연습을 반복해야겠다.

import heapq

n = int(input())
plist = list(map(int,input().split()))
cost = int(input())

hq = []
heapq.heapify(hq)
for idx, p in enumerate(plist):
    heapq.heappush(hq, (p,idx))


min_cost, min_idx = min((p, i) for i, p in enumerate(plist))
min_nonzero_cost, min_nonzero_idx = None, None
for i in range(1, n):
    if min_nonzero_cost is None or plist[i] < min_nonzero_cost:
        min_nonzero_cost, min_nonzero_idx = plist[i], i


if n == 1:
    print(0 if cost >= plist[0] else 0)
    exit()
if cost < min_nonzero_cost:
    print(0 if cost >= plist[0] else 0)
    exit()

length = 1 + (cost - min_nonzero_cost) // min_cost
ans = [min_idx] * length
ans[0] = min_nonzero_idx
left = cost - (min_nonzero_cost + (length - 1) * min_cost)

for pos in range(length):
    for d in range(n - 1, -1, -1):
        need = plist[d] - plist[ans[pos]]
        if need <= left and (pos > 0 or d != 0): 
            ans[pos] = d
            left -= need
            break

print(''.join(str(d) for d in ans))