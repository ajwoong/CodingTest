n,m = map(int, input().split())
nlist = list(map(int, input().split()))

start = 0 
end = 0
answer = 0

while(end < len(nlist)):
    if(start <= end):
        if(sum(nlist[start:end+1]) < m):
            end += 1
        elif(sum(nlist[start:end+1]) > m):
            start += 1
        else:
            answer += 1
            end += 1
    else:
        end = start


print(answer)