# 년, 월, 일 설정이 까다로웠던 문제
# 파이썬의 date 자료형으로 날짜를 비교 가능하다는 사실을 알음
# 그냥 모든걸 일로 환산해서 계산 후 비교할걸 그랬다는 생각이 들음

from datetime import date

today = "2023.01.01"
terms = ["A 6"]
privacies = 	["2022.07.01 A", "2022.07.01 A", "2022.07.01 A"]

answer = []
todayList = today.split(".")

x = 1
for privacy in privacies:
    privacyList = privacy.split()
    for term in terms:
        termList = term.split(" ")
        if(termList[0] == privacyList[1]):
            privacyDateList = privacyList[0].split(".")

            privacyDateListYear = int(privacyDateList[0])
            privacyDateListMonth = int(privacyDateList[1]) + int(termList[1])
            privacyDateListDay = int(privacyDateList[2])
            

            while(privacyDateListMonth > 12):
                privacyDateListMonth = privacyDateListMonth - 12
                privacyDateListYear += 1
            
            if(privacyDateListDay - 1 <= 0):
                if(privacyDateListMonth == 1):
                    privacyDateListMonth = 12
                    privacyDateListYear -= 1
                else:
                    privacyDateListMonth -= 1
                privacyDateListDay = 28

            else:
                privacyDateListDay -= 1
            
            todayListYear = int(todayList[0])
            todayListMonth = int(todayList[1])
            todayListDay = int(todayList[2])

            print(privacyDateListYear, privacyDateListMonth, privacyDateListDay)

            todayDate = date(todayListYear, todayListMonth, todayListDay)
            privacyDate = date(privacyDateListYear, privacyDateListMonth, privacyDateListDay)

            if(todayDate > privacyDate):
                answer.append(x)
            break

    x += 1

print(answer)
            
            

