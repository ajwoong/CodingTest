# 스택으로 어찌저찌 구현했지만, 시간초과가 발생
# 생각해보니 끝에서부터 상자를 수거, 상자를 배송하고 cap 만큼 빼면 되는거였음
# 그리고 cap 만큼 빼는 그 위치에서 수거, 배송한거니까 왕복으로 * 2하면 디는거였다.

cap = 1
n = 5
deliveries = 	[0, 0, 1, 0, 0]
pickups =    [0, 0, 0, 0, 0]

total = 0

while True:
    deliverySum = 0
    deliveryEndPoint = -1
    pickupSum = 0
    pickupEndPoint = -1
    for x in range(n-1, -1, -1):
        if(deliverySum + deliveries[x] <= cap):
            if(deliveries[x] !=0 ):
                deliverySum += deliveries[x]
                deliveryEndPoint = max(deliveryEndPoint, x)
                deliveries[x] = 0
        else:
            while(deliverySum != cap):
                deliveryEndPoint = max(deliveryEndPoint, x)
                deliverySum += 1
                deliveries[x] -= 1

        if(pickupSum + pickups[x] <= cap):
            if(pickups[x] !=0 ):
                pickupSum += pickups[x]
                pickupEndPoint = max(pickupEndPoint, x)
                pickups[x] = 0
        else:
            while(pickupSum != cap):
                pickupEndPoint = max(pickupEndPoint, x)
                pickupSum += 1
                pickups[x] -= 1
        
    
    if(deliveryEndPoint == -1 and pickupEndPoint == -1):
        break

    if(deliveryEndPoint >= pickupEndPoint):
        total += (deliveryEndPoint + 1) * 2
    else:
        total += (pickupEndPoint+ 1) * 2

print(total)