n = int(input())

tlist = list(map(int,input().split()))
oktlist = list(map(int,input().split()))


idx = 0
ans = []
while idx < len(tlist):
    if(oktlist[idx] - tlist[idx] > 0):
        pls_time = True
        max_time = oktlist[idx] - tlist[idx]
        break

    elif(tlist[idx] - oktlist[idx] > 0):
        pls_time = False
        max_time = tlist[idx] - oktlist[idx]
        break

    else:
        idx += 1
        continue

ans = []
while idx < len(tlist):
    if(oktlist[idx] - tlist[idx] > 0):
        if(pls_time):
            k = max(max_time, oktlist[idx] - tlist[idx])
            if(k > max_time):
                max_time = k
                ans.append(max_time)
        else:
            pls_time = True
            ans.append(max_time)
            max_time = oktlist[idx] - tlist[idx]
    elif(tlist[idx] - oktlist[idx] > 0):
        if(not pls_time):
            k = max(max_time, tlist[idx] - oktlist[idx])
            if(k > max_time):
                max_time = k
                ans.append(max_time)
        else:
            pls_time = False
            ans.append(max_time)
            max_time = tlist[idx] - oktlist[idx]
    idx += 1

if(max_time != 0):
    ans.append(max_time)

print(sum(ans))
