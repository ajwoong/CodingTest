# 첫 level 3 문제였는데, 평가는 되게 쉬운 문제라고 한다
# 나는 틀렸다. dp문제인데, dp는 확실히 Top-down과 bottom-up 어프로치 중에 선택해서 풀어야한다.
# 삼각형을 밑에서부터 위로 큰 값들을 선택해서 더해주면 되는 방식이었다.
# dp문제에 익숙해지도록 해야겠다

def solution(triangle):
    newTriangle = triangle[::-1]
    
    for x in range(len(newTriangle)-1):
        for y in range(len(newTriangle[x])-1):
            newTriangle[x+1][y] += max(newTriangle[x][y], newTriangle[x][y+1])
    
    return newTriangle[-1][0]