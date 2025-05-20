# 이 문제는 이전에 프로그래머스에서 본 stack활용 문제이다.
# 그때도 유형이 너무 까다로워서 풀지 못했는데, 외웠다고 생각했는데 제대로 외우지 못해 다시 풀었을때 틀렸다.
# 스택을 활용하는 문제는 answer, nlist, stack 이렇게 세가지 배열을 두고 인덱스를 가져와서 업데이트 하는 방식으로 처리한다는것을
# 기억해두면 앞으로 문제를 풀때 헷갈리지 않을 것 같다.

n = int(input())
numbers = list(map(int,input().split()))


answer = [-1] * len(numbers)
stack = []

for x in range(len(numbers)):
    target = numbers[x]

    while stack and numbers[stack[-1]] < target:
        answer[stack.pop()] = target
    
    stack.append(x)

for x in answer:
    print(x, end=" ")