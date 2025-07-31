# 제일 아쉬움이 많이 남은 문제, 끝까지 해결할 방법을 찾아 최적화에 성공했지만 제출을 못함
# 자연수 n이 주어졌을때 이진수로 n을 변환했을때 1의개수가 같고, n보다 작은 자연수들의 개수를 구하는 문제
# 내 풀이법은 10100 이렇게 주어지면 문자열을 처음부터 탐색하면서 1을 만난다면 (남은 문자열 개수)C(남은 1 개수) 를 다 더하는 것
# 여기서는 4C2 + 2C1이 되겠다.


from math import comb

def solution(n):
    binary = format(n, 'b')
    length = len(binary)
    one_count = binary.count("1")
    count = 0

    for i in range(length):
        if(binary[i] == '1'):
            if(length-i-1 >0):
                count += comb(length-i-1, one_count)
            one_count -= 1

    return count

n = int(input())
print(solution(n))