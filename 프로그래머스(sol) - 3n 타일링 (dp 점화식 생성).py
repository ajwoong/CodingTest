# dp 문제
# 구현 뿐 아니라 아이디어 까지 답을 본 문제다
# dp 문제는 점화식 설정이 가장 중요한데, 수학적 사고를 더 길러서 점화식을 잘 설정할 수 있도록 해야겠다.

n = int(input())

answer = [0, 3, 11]
index = int(n/2)

if(n%2 != 0 ):
    print(0)
if(index<3) : print(answer[index])

for x in range(3, index+1):
    answer.append((3*answer[x-1] + sum(answer[1:x-1]) *2 + 2 ) % 1000000007)

print(answer[index])