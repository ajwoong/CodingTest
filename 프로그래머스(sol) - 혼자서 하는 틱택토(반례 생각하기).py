# 틱택토의 답이 두개가 되는 경우를 간과했다
# 답이 두개면 무조건 안되는줄 알았는데 하나의 표기로 틱택토가 두개가 완성되는 경우가 있었다.
# 더 꼼꼼히 살펴보고 조건을 확인해야겠다

board = ["OOO", "OXX", "OXX"]


solvedO = 0
solvedX = 0
realNumO = 0
realNumX = 0

for x in range(3):
    numO = 0
    numX = 0
    for y in range(3):
        if(board[x][y] == 'O'):
            realNumO += 1
            numO += 1
        elif (board[x][y] == 'X'):
            realNumX += 1
            numX += 1
    if(numO == 3):
        solvedO += 1
    if(numX == 3):
        solvedX += 1

for x in range(3):
    numO = 0
    numX = 0
    for y in range(3):
        if(board[y][x] == 'O'):
            numO += 1
        elif (board[y][x] == 'X'):
            numX += 1
    if(numO == 3):
        solvedO += 1
    if(numX == 3):
        solvedX += 1

if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and (board[1][1] == 'O')):
    solvedO += 1

if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and (board[1][1] == 'X')):
    solvedX += 1

if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and (board[1][1] == 'O')):
    solvedO += 1

if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and (board[1][1] == 'X')):
    solvedX += 1

solved = solvedO + solvedX

if(solved>1 or realNumO < realNumX):
    if(solvedO == 2 and solvedX == 0 and realNumO == realNumX + 1):
        print(1)
    print(0)

else:
    if(realNumO - realNumX > 1) or (solvedX == 1 and realNumO > realNumX) or (solvedO == 1 and realNumO == realNumX):
        print (0)
    else:
        print(1)