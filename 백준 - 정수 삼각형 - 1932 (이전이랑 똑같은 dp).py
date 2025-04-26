import sys
input = sys.stdin.readline

n = int(input())

triangle = []
for i in range(n):
    k = list(map(int,input().split()))
    triangle.append(k)


for x in range(len(triangle) - 1 , 0 , -1):
    for y in range(len(triangle[x])-1):
        triangle[x-1][y] += max(triangle[x][y], triangle[x][y+1])

print(triangle[0][0])