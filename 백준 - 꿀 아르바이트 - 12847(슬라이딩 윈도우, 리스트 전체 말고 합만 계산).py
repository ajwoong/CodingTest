n,m = map(int,input().split())
nlist = list(map(int,input().split()))


max_money = sum(nlist[0:m])
new_max_money = max_money
start = 0
end = m - 1

while True:
    new_max_money -= nlist[start]
    start+=1
    end += 1
    if(end >= len(nlist)):
        break
    new_max_money += nlist[end]
    max_money = max(max_money, new_max_money)

print(max_money)