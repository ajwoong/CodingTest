# 조이스틱을 오른쪽 왼쪽 움직이는 거의 최솟값을 구해야 풀 수 있는 문제였다
# 연속된 A를 마주했을때 가장 긴 연속된 A의 왼쪽에서 꺾기 OR 그 A의 오른쪽에서 꺾기 OR 기존 이걸로 구할 수 있다

name = input()

alphabet = {}

for x in range(65, 91):
    alphabet[chr(x)] = x - 65

answer = 0
notAnum = 0
leftRight = len(name) - 1

for char in name:
    alphabetIndex = alphabet[char]
    reverseAlphabetIndex = 25 - alphabet[char] + 1
    
    if(alphabetIndex < reverseAlphabetIndex):
        answer += alphabetIndex
    else:
        answer += reverseAlphabetIndex
    
    if(char != 'A'):
        notAnum += 1


for x in range(len(name)):
    next = x + 1
    while (next < len(name) and name[next] == 'A'):
        next += 1

    leftRight = min(leftRight, 2*x + len(name) - next, x + 2 *(len(name) - next))



print(answer + leftRight)