# 주어진 변수의 크기가 크지 않으므로 완전 탐색 가능
# 이차원 배열에서 한 위치마다 각각 전부 돗자리 만들수 있을지 검색하는 방식으로 해결

mats = [5, 3, 2]

park = [["A", "A", "-1", "B", "B", "B", "B", "-1"], 
        ["A", "A", "-1", "B", "B", "B", "B", "-1"], 
        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], 
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], 
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], 
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]


def makeMat(mat, x, y):
    for matColumn in range(mat):
        for matRow in range(mat):
            if(x+matColumn < len(park) and y+matRow < len(park[0])):
                if(park[x+matColumn][y+matRow] != "-1"):
                    return False
            else:
                return False
    
    return True


result = []
for mat in mats:
    for x in range(len(park)):
        for y in range(len(park[0])):
            boolMakeMat = makeMat(mat, park, x, y)
            if(boolMakeMat == True):
                 result.append(mat)

if(result == []):
    print(-1)
else:
    print(max(result))