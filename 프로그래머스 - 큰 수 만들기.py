# 그리디 활용했는데 마지막 테스트 케이스인 k가 다 소모되지않고 계속 작은거만 나오는 경우가 있었다.
# 이를 예외 처리해서 문제를 해결했는데, 반례 케이스를 머리속으로 잘 생각해보는 능력을 길러야겠다.

number = "11231111110"
k = 3

numberList = list(number)

start = numberList[0]
numberList = numberList[1:]
answer = [start]


i = 1
for x in numberList:
    if(int(start) < int(x)):
        while(answer and int(answer[-1]) < int(x) and k >= 1):
            answer.pop()
            k -= 1
        answer.append(x)
        start = x
    else:
        answer.append(x)
        start = x
    if(k <= 0):
        break
    i += 1

if(k > 0):
    print(''.join(answer[:len(answer) - k]))
else:
    print(''.join(answer + numberList[i:]))