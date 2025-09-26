# 또다른 완전탐색 중간 난이도의 문제였다.
# 시간복잡도를 계산해 완전탐색을 해도 괜찮은지 파악하는게 항상 관건인것같다.
# 조합을 nC0부터 nCn까지 더한 값이 2^n 인것을 기억해서, 시간복잡도 계산을 통해 조합으로 풀었다.

from itertools import combinations
import math

t = input()
n = int(input())

book_list = []
for i in range(n):
    price, book = input().split()
    book_list.append((int(price), book))

answer = math.inf
for i in range(1,n+1):
    comb = combinations(book_list, i)
    for c in comb:
        combined_word = ""
        combined_cost = 0
        target = t
        make_word = False
        for cost, book in c:
            combined_word += book
            combined_cost += cost
        for word in t:
            if(word in combined_word):
                idx = combined_word.index(word)
                combined_word = combined_word[:idx] + combined_word[idx+1:]
                idx_t = target.index(word)
                target = target[:idx_t] + target[idx_t+1:]
        if(target == ""):
            make_word = True
        if(make_word):
            answer = min(answer, combined_cost)

if(answer == math.inf):
    print(-1)
else:
    print(answer)