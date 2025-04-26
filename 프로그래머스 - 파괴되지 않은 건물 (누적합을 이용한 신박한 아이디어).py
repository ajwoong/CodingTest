# 처음에 3중 포문을 사용했을 때는 당연히 시간초과가 발생하였다.
# 그만큼 누적합의 아이디어가 매우 중요한 문제였다.
# 어떤 이차원 배열의 영역에 더하고 싶은 값이 있다면, 예를들어 (0,0)부터 (3,4)까지의 영역에 2를 더하고 싶다면
# (0,0)을 2 (0,5)를 -2 (0,3)을 -2 (3,4)를 2로 설정하고
# 각 행마다 누적합을 하고, 그 이후 각 열마다 누적합을 구하면 해당 전체 영역에 2를 더할 수 있게 된다.
#
# 1. (x1,y1), (x2+1,y2+1)에 2 (x1,y2+1), (x2,y1+1)에 -2 설정
# [2, 0, 0, -2]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [-2, 0, 0, 2]
#
# 2. 각 행의 누적합을 구하기
# [2, 2, 2, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [-2, -2, -2, 0]
# 
# 3. 각 열의 누적합을 구하기
# [2, 2, 2, 0]
# [2, 2, 2, 0]
# [2, 2, 2, 0]
# [0, 0, 0, 0]

# 이 방식을 통해 기존에 시간복잡도가 skill * board행 * board열 만큼 걸린 시간복잡도를
# skill + (board행 * board열)의 시간복잡도로 고치게 되었다.

def solution(board, skill):
    
    add_board = [[0 for _ in range(len(board[0]) + 1)]  for _ in range(len(board) + 1)]
    
    for s in skill:
        if(s[0] == 1):
            add_board[s[1]][s[2]] += s[5] * (-1)
            add_board[s[3] + 1][s[2]] += s[5]
            add_board[s[1]][s[4] + 1] += s[5]
            add_board[s[3]+1][s[4] + 1] += s[5] * (-1)
        if(s[0] == 2):
            add_board[s[1]][s[2]] += s[5]
            add_board[s[3] + 1][s[2]] += s[5] * (-1)
            add_board[s[1]][s[4] + 1] += s[5] * (-1)
            add_board[s[3]+1][s[4] + 1] += s[5]
    

    for i in range(len(add_board) - 1):
        for j in range(len(add_board[0]) - 1):
            add_board[i][j + 1] += add_board[i][j]
            
    for j in range(len(add_board[0]) - 1):
        for i in range(len(add_board) - 1):
            add_board[i+1][j] += add_board[i][j]
            
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += add_board[i][j]
            if(board[i][j] > 0):
                answer += 1
    
    return answer    
