def solution(places):
    
    new_places = []
    for p in places:
        pList = []
        for i in p:
            pList.append(list(i))
        new_places.append(pList)
    
    dx1 = [0,0,1,-1]
    dy1 = [1,-1,0,0]
    
    dx2 = [0,0,2,-2]
    dy2 = [2,-2,0,0]
    
    dx3 = [1,1,-1,-1]
    dy3 = [1,-1,-1,1]
    
    
    def check1(x,y,p):
        
        for k in range(4):
            nx = x + dx1[k]
            ny = y + dy1[k]
            if(nx<len(p) and ny<len(p[0]) and nx>=0 and ny>=0):
                if(p[nx][ny] == "P"):
                    return False
                
        
            nx = x + dx2[k]
            ny = y + dy2[k]
            if(nx<len(p) and ny<len(p[0]) and nx>=0 and ny>=0):
                if(p[nx][ny] == "P"):
                    mx = x + dx1[k]
                    my = y + dy1[k]
                    if(p[mx][my] != "X"):
                        return False
            
            nx = x + dx3[k]
            ny = y + dy3[k]
            if(nx<len(p) and ny<len(p[0]) and nx>=0 and ny>=0):
                if(p[nx][ny] == "P"):
                    if(k == 0):
                        if(p[nx + 1][ny] != 'X' or p[nx][ny+1] != 'X'):
                            return False
                    if(k==1):
                        if(p[nx+1][ny] != 'X' or p[nx][ny-1]!='X'):
                            return False
                    if(k==2):
                        if(p[nx][ny-1] != 'X' or p[nx-1][ny] !='X'):
                            return False
                    if(k==3):
                        if(p[nx-1][ny] != 'X' or p[nx][ny+1] != 'X'):
                            return False
                                   
        return True
        
        
            
    check = True
    answer = []
    for p in new_places:
        for i in range(len(p)):
            for j in range(len(p[0])):
                if(p[i][j] == "P"):
                    check = check1(i,j, p)
                    if(check == False):
                        break
                        
            if(check == False):
                answer.append(0)
                break
            else:
                answer.append(1)
                break
                
    
    return(answer)
                


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])