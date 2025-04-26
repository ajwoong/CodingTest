# 또 dp를 틀렸다. 진짜 미치겠다. 이진법으로 변환후에 누적으로 비트연산해서 구하려고 했지만, 해당 방식은 적합하지 않았다.
# 정사각형 후보의 한점에서 왼,위, 대각선위의 숫자를 보고 해당 숫자중 최소값 + 1을 하면 해당 지점에서 만들 수 있는 정사각형 수다
# 이유는 처음 1인지점을 볼때 가장 작은 2*2 부분을 보면 해당 지점에서 2*2 정사각형이 만들어지는 보고 이게 점차 넓어져서 그렇게 될 수 있다.
# 계속 dp를 틀리니까 너무 힘들지만, 언젠가는 될거라는 생각으로 해야겠다.

from copy import deepcopy

def solution(board):
    
    
    if not board or not board[0]:
        return 0

    if len(board) == 1 or len(board[0]) == 1:
        return 1 if any(1 in row for row in board) else 0
    
    
    answer = 0
    dp = deepcopy(board)
    for x in range(1,len(board)):
        for y in range(1,len(board[0])):
            if(dp[x][y] == 1):
                dp[x][y] = min(dp[x-1][y], dp[x-1][y-1], dp[x][y-1]) + 1
                answer = max(answer, dp[x][y])
    
    answer = max(answer, max(max(row) for row in board))
    return answer ** 2
    
            