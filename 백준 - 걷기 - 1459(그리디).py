x, y, w, s = map(int,input().split())

cost = 0

if(x>=y):
    leftx = x - y
    if(2*w>=s):
        cost += (y * s)
        if(w>=s):
            a = leftx // 2
            b = leftx % 2 
            cost += (a*s*2)
            cost += (b*w)
        else:
            cost += (leftx * w)
    else:
        cost += ((x+y) * w)

else:
    lefty = y - x
    if(2*w>=s):
        cost += (x * s)
        if(w>=s):
            a = lefty // 2
            b = lefty % 2 
            cost += (a*s*2)
            cost += (b*w)
        else:
            cost += (lefty * w)
    else:
        cost += ((x+y) * w)

print(cost)
    
