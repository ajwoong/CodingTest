# 가장 가까이있는 이라는 키워드를 가지고 stack을 활용한 문제임을 깨닫는 것이 중요하다.
# stack을 활용해 answer를 업데이트 해 나가는 것을 기억하면 좋다.

numbers = [2, 3, 3, 5]

answer = [-1] * len(numbers)
stack = []

for x in range(len(numbers)):
    target = numbers[x]

    while stack and numbers[stack[-1]] < target:
        answer[stack.pop()] = target
    
    stack.append(x)

print(answer)