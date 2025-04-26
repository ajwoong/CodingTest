friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

giftArray = [[0 for _ in range(len(friends))] for _ in range(len(friends)) ]

for gift in gifts:
    newGift = gift.split()
    giftArray[friends.index(newGift[0])][friends.index(newGift[1])] += 1


nextMonthGift = [0 for _ in range(len(friends))]
giftIndices = [0 for _ in range(len(friends))]
i = 0

for giftList in giftArray:
    for k in giftList:
        giftIndices[i] += k
    i += 1

p = 0
for a in range(0, len(friends)):
    for b in range(0, len(friends)):
        giftIndices[p] -= giftArray[b][a]
    p += 1


for x in range(0, len(friends)):
    for y in range(x+1, len(friends)):
        if(giftArray[x][y] > giftArray[y][x]):
            nextMonthGift[x] += 1
        elif(giftArray[x][y] < giftArray[y][x]):
            nextMonthGift[y] += 1
        else:
            if(giftIndices[x] > giftIndices[y]):
                nextMonthGift[x] += 1
            elif(giftIndices[x] < giftIndices[y]):
                nextMonthGift[y] += 1
