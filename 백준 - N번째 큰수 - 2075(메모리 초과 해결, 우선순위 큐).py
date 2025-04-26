import sys, heapq
input = sys.stdin.readline

n = int(input())


hq = []

for i in range(n):
    arr = list(map(int,input().split()))
    for j in arr:
        heapq.heappush(hq, j)
        if(len(hq) > n):
            heapq.heappop(hq)
        
print(hq[0])