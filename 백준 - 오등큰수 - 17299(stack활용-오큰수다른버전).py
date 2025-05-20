# 금방 오큰수 문제를 풀어 오등큰수 문제는 쉽게 풀 수 있었다.
# 스택을 활용해 3개의 배열을 가지고 푸는 이 방법을 꼭 외워야겠다.
# 외우다 보면 자연스럽게 이해가 될것이다.

from collections import Counter

n = int(input())
nlist = list(map(int,input().split()))

counter = Counter(nlist)
n_nlist = []

for i in nlist:
    n_nlist.append([i, counter[i]])

answer = [-1] * n
stack = []

for i in range(n):
    target = n_nlist[i]

    while(stack and n_nlist[stack[-1]][1]< target[1]):
        answer[stack.pop()] = target[0]

    stack.append(i)

for i in answer:
    print(i, end=" ")