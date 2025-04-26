# 단순 구현으로 풀긴했지만, 시간 초과가 났다.
# 그리디를 그래서 생각해 보았다.

def solution(n, stations, w):
    
    nList = [0] * n
    
    for i in stations:
        i = i - 1
        if(i+w < n and i -w >= 0):
            for j in range(i-w, i+w+1,1):
                nList[j] = 1
        elif(i +w < n and i - w < 0):
            for j in range(0, i + w + 1, 1):
                nList[j] = 1
        elif(i+w>=n and i-w>=0):
            for j in range(i-w, n, 1):
                nList[j] = 1
        elif(i+w>=n and i-w<0):
            for j in range(0,n,1):
                nList[j] = 1
    
    answer = 0
    for i in range(n):
        if(nList[i] == 0):
            if(i + w >= n):
                answer += 1
                for j in range(i,n,1):
                    nList[j] = 1
            else:
                if(nList[i+w] == 0):
                    answer += 1
                    if(i+ w + w < n):
                        for j in range(i, i + w + w + 1, 1):
                            nList[j] = 1
                    else:
                        for j in range(i, n, 1):
                            nList[j] = 1
                else:
                    answer += 1
                    if(i+w < n and i -w >= 0):
                        for j in range(i-w, i+w+1,1):
                            nList[j] = 1
                    elif(i +w < n and i - w < 0):
                        for j in range(0, i + w + 1, 1):
                            nList[j] = 1
                    elif(i+w>=n and i-w>=0):
                        for j in range(i-w, n, 1):
                            nList[j] = 1
                    elif(i+w>=n and i-w<0):
                        for j in range(0,n,1):
                            nList[j] = 1
                    
                        
    return answer
             