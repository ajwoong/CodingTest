# 자기보다 처음으로 작아지는 숫자의 인덱스값을 answer에 저장하고
# 해당 answer를 현재 자기의 인덱스와 비교하는 방식으로 코드를 구성했다.
# 뒤에 있는 큰 수 찾기와 유사한 스텍 문제이기 때문에 해당 스텍을 활용하는 방식을 제대로 알아야겠다.

prices = [1,2,3,2,3]

answer = [-1] * len(prices)
stack = []

for x in range(len(prices)):

    target = prices[x]

    while(stack and prices[stack[-1]] > target):
        answer[stack.pop()] = x

    stack.append(x)



for x in range(len(prices)):
    if(answer[x] == -1):
        answer[x] = (len(prices) - 1) - x
    else:
        answer[x] = answer[x] - x


print(answer)