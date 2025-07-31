# aaabbbbcdddefffg
# 이런식으로 주어졌을때 중복이 있는 것들은 a* 이런식으로 바꾸는 문제
# a*b*cd*ef*g 답은 이렇게 될것임

def solution(line):
    answer = ""
    check = 0

    while check < len(line) - 1:
        now = line[check]
        answer += now
        is_multiple = 0
        check += 1

        while check < len(line) and line[check] == now:
            is_multiple += 1
            check += 1

        if is_multiple > 0:
            answer += '*'

    if check == len(line) - 1:
        answer += line[check]

    return answer

s = input()
print(solution(s))