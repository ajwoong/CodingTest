# 문제의 개념은 피보나치수와 똑같았다.
# 그런데 시간초과가 문제였더니 알고보니, 기하급수적으로 커지는 피보나치수의 연산량에 시간을 많이 쓰게 되니 15746으로 미리
# 나머지를 구해서 피보나치 배열을 돌리는 방식이었다.
# 추가적으로 메모리제한까지 있어 dp 배열을 쓸수가 없었다. 그래서 더 까다로운 문제였다.

n = int(input())

first = 1
second = 2

if(n == 1):
    print(first % 15746)

else:
    for i in range(2,n):
        first, second = second, (first+second) % 15746
    print(second)