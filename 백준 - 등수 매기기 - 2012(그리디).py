import sys
input = sys.stdin.readline

n = int(input())
blist = []

for i in range(n):
    b = int(input())
    blist.append(b)

blist.sort()

answer = 0
rank = 1
for b in blist:
    answer += abs(rank - b)
    rank+=1

print(answer)