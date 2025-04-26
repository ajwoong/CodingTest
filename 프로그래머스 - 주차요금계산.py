from collections import defaultdict
import math

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", 
           "06:00 0000 IN", 
           "06:34 0000 OUT", 
           "07:59 5961 OUT", 
           "07:59 0148 IN", 
           "18:59 0000 IN", 
           "19:09 0148 OUT", 
           "22:59 5961 IN", 
           "23:00 5961 OUT"]


dict = defaultdict(list)
answerList = []

for record in records:
    recordList = record.split(" ")
    dict[recordList[1]].append([recordList[0], recordList[2]])

for key, value in dict.items():
    lastIsIn = 0
    answer = 0
    for check in value:
        if(check[1] == 'IN'):
            checkList = check[0].split(":")
            hour = int(checkList[0]) * 60
            minute = int(checkList[1])
            timeCheck = hour + minute
            lastIsIn = 1
        elif(check[1] == 'OUT'):
            checkList = check[0].split(":")
            hour = int(checkList[0]) * 60
            minute = int(checkList[1])
            timeCheck = hour + minute - timeCheck
            answer += timeCheck
            lastIsIn = 0
    
    
    if(lastIsIn == 1):
        hour = 23 * 60
        minute = 59
        timeCheck = hour + minute - timeCheck
        answer = answer + timeCheck

    answerList.append([key, answer]) 
    answerList.sort()


paymentList = []
for time in answerList:
    if(time[1] <= fees[0]):
        payment = fees[1]
    else:
        payment = (math.ceil((time[1] - fees[0])/fees[2])) * fees[3] + fees[1]
    paymentList.append(payment)

print(paymentList)