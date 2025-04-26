board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

bag = []
answer = 0
for move in moves:
    for x in range(len(board)):
        if(board[x][move - 1] != 0 ):
            bag.append(board[x][move-1])
            board[x][move-1] = 0
            break
    
    if(len(bag) >= 2):
        if(bag[-1] == bag[-2]):
            bag.pop()
            answer+=1
            bag.pop()
            answer+=1
    
        
        