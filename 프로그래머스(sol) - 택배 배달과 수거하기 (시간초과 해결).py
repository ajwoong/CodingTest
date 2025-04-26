cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]	
pickups = [0, 3, 0, 4, 0]	


answer = 0
delivery = 0
pickup =0

for x in range(n-1, -1, -1):
    delivery += deliveries[x]
    pickup += pickups[x]

    while delivery > 0 or pickup > 0:
        delivery -= cap
        pickup -= cap
        answer += (x+1) * 2

print(answer)