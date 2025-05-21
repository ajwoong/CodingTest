# 엄청난 고민 끝에 끝내 해결한 문제이다.
# 스택을 활용하는 문제로, 생각하지 못한건 폭발 문자열의 길이가 1일때를 생각하지 못했다.
# 그 부분 외에 예외처리 및 구현은 잘 해냈다.

n = input()
dn = input()

stack = []

if len(dn) == 1:
    answer = n.replace(dn, "")
    if answer:
        print(answer)
    else:
        print("FRULA")

else:
    for i in range(len(n)):

        if(not stack):
            if(n[i] == dn[0]):
                stack.append(0)
            else:
                stack.append(n[i])

        else:
            if(type(stack[-1]) == int  and stack[-1] < len(dn) - 1  and n[i] == dn[stack[-1] + 1]):
                if(stack[-1] + 1 == len(dn) - 1):
                    while(stack and stack[-1] != 0):
                        stack.pop()
                    if(stack and stack[-1] == 0):
                        stack.pop()
                else:
                    stack.append(stack[-1] + 1)

            else:
                if(n[i] == dn[0]):
                    stack.append(0)
                else:
                    stack.append(n[i])         

    if stack:
        for i in stack:
            if(type(i) == int):
                print(dn[i], end="")
            else:
                print(i, end = "")

    else:
        print("FRULA")