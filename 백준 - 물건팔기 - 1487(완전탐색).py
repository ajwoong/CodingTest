# 조건을 잘 생각해야 하는 완전탐색 문제였다.

import math
n = int(input())

plist = []
start = math.inf
end = -1 * math.inf
max_price = 0
for i in range(n):
    pay, send = map(int, input().split())
    if(pay > send):
        plist.append((pay,send))
        start = min(start, pay)
        end = max(end, pay)


if(not plist):
    print(max_price)

else:
    new_price_list = []
    for price in range(start, end+1):
        new_price = 0
        for pay, send in plist:
            if(price <= pay):
                if(price - send > 0):
                    new_price += (price - send)
        if(new_price > max_price):
            new_price_list.append((price, new_price))
            max_price = max(max_price, new_price)

    new_price_list.sort(key = lambda x:(x[1], -x[0]), reverse=True)
    print(new_price_list[0][0])