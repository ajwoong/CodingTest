players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]


answer = []
playersDict = {}


for x in range(len(players)):
    playersDict[players[x]] = x
    

for call in callings:
    callIndex = playersDict[call] # 앞 지를 사람의 인덱스
    a = players[callIndex]  # 앞 지르는 사람 찾기
    b = players[callIndex - 1]  # 앞 지름 당하는 사람 찾기

    players[callIndex - 1] = a 
    players[callIndex] = b
    # 둘이 위치 바꾸기 

    playersDict[a] = callIndex - 1
    playersDict[b] = callIndex


for x in range(len(players)):
    answer.append(players[x])

print(answer)