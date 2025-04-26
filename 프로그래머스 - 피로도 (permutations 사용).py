from itertools import permutations

k = 80
dungeons = [[80,20],[50,40],[30,10]]	

dungeonList = permutations(dungeons, 3)

answer = 0
for x in dungeonList:
    health = k
    newAnswer = 0
    for y in x:
        if(y[0] <= health):
            health -= y[1]
            newAnswer += 1
        else:
            break
    answer = max(answer, newAnswer)

print(answer)