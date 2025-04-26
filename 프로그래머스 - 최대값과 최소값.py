s = "-1 -2 -3 -4"

sList = s.split(" ")
sNumList = []
for x in sList:
    sNumList.append(int(x))

min = min(sNumList)
max = max(sNumList)

answer = str(min) + " " + str(max)
print(answer)