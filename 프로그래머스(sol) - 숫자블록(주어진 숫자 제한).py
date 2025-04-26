# 제곱근까지 개산해서 약수 중 최고 큰거를 찾는 문제라는 점은 깨달았다
# 하지만 문제에서 주어진 조건으로 보면 약수가 천만이상이 된다면 그값보다는 작은 약수를 answer에 추가해야한다.
# 그 이유는 문제가 천만까지로 제한이 걸려있기 때문이다. 항상 문제에서 주어진 조건을 잘 봐야겠다

begin, end = map(int, input().split())

answer = []
for number in range(begin, end+1):
    ans = [1]
    if(number == 1):
        answer.append(0)
    else:
        for x in range(2, int(number ** (1/2)) + 1):
            if((number % x == 0) and x <= 1e7):
                ans.append(x)
                if (number//x <= 1e7 and number//x != number):
                    ans.append((number // x))

        answer.append(max(ans))

print(answer)