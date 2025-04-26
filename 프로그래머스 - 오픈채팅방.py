record = ["Enter uid1234 Muzi", 
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]


dict  = {}
answerList = []

for sentence in record:
    sentenceList = sentence.split()
    if(sentenceList[0] == 'Enter'):
        dict[sentenceList[1]] = sentenceList[2]
    elif(sentenceList[0] == 'Leave'):
        del sentenceList[1]
    elif(sentenceList[0] == 'Change'):
        dict[sentenceList[1]] = sentenceList[2]


for sentence in record:
    sentenceList = sentence.split()
    answer = ""
    if(sentenceList[0] == 'Enter'):
        answer = dict[sentenceList[1]] + "님이 들어왔습니다."
        answerList.append(answer)
    elif(sentenceList[0] == 'Leave'):
        answer = dict[sentenceList[1]] + "님이 나갔습니다."
        answerList.append(answer)


print(answerList)