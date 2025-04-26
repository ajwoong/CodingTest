# 3진법으로 생각하는 접근은 맞아지만 0이 없어서 수학적으로 생각을 못했음
# 3으로 나누어떨어지면 몫을 -1 시키고 나머지를 3으로 만들면 되는 것이었다

n = int(input())
answer = ""

while True:
    if(n % 3 != 0 ):
        answer += str(n%3)
        n = n // 3
    else:
        answer += str(3)
        n = n // 3 - 1
    
    if(n<3):
        if(n != 0):
            answer += str(n)
        break

answerList = list(answer)
answerList.reverse()

realAnswer = ""
for x in answerList:
    if(x=="3"):
        realAnswer += "4"
    else:
        realAnswer += x

print(realAnswer)