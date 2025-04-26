# 반례를 찾았는데도 구현을 잘못해서 반례를 찾아봤다
# 구현을 더 잘하자

picks = [0,1,1]
minerals = ["iron", "iron", "stone", "stone", "stone",
            "diamond", "diamond", "diamond", "diamond", "stone",
            "diamond", "diamond", "diamond", "diamond", "diamond"]


# picks = [0,1,1]
# minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]


mineralsList = []
for index in range(0, len(minerals), 5):
    appendList = [0, 0, 0]
    for x in range(index, index+5):
        if(x > len(minerals) - 1):
            break
        if(minerals[x] == 'diamond'):
            appendList[0] += 1
        elif(minerals[x] == 'iron'):
            appendList[1] += 1
        elif(minerals[x] == 'stone'):
            appendList[2] += 1
    mineralsList.append(appendList)


if(sum(picks) > 1):
    if(sum(picks) * 5 < len(minerals)):
        k = mineralsList.pop()
        mineralsList.sort(reverse=True)
        mineralsList.append(k)
    else:
        mineralsList.sort(reverse=True)
    


print(mineralsList)

i = 0
answer = 0
for k in mineralsList:
    while(i<= 2 and picks[i] == 0):
        i+=1
    if(i == 0):
        picks[i] -= 1
        answer += k[0] * 1
        answer += k[1] * 1
        answer += k[2] * 1
    elif(i == 1):
        picks[i] -= 1
        answer += k[0] * 5
        answer += k[1] * 1
        answer += k[2] * 1
    elif(i == 2):
        picks[i] -= 1
        answer += k[0] * 25
        answer += k[1] * 5
        answer += k[2] * 1
    if(i>=3):
        break

print(answer, mineralsList)