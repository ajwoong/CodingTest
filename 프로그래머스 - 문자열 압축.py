# string을 슬라이싱 할때, 범위 밖이어도 오류가 나지않고 빈 문자열로 등록된다.
# 런타임에러가 나온다면 배열의 잘못된 인덱스에 접근했다고 생각하자.
# 항상 반례를 생각할때는 극적인 값으로 접근해야한다. 

def solution(s):
    measure = len(s) // 2
    
    answer = []
    
    for m in range(1, measure+1, 1):
        repeatString = s[0:m]
        repeat = 1
        answerString = ""
        
        for x in range(m,len(s)+m,m):
            if(repeatString == s[x: x + m]):
                repeat += 1
            else:
                if(repeat == 1):
                    answerString = answerString + repeatString
                else:
                    answerString = answerString + str(repeat) + repeatString
                repeat = 1
                repeatString = s[x: x + m]
        
        answer.append(answerString)
    
    answer = sorted(answer, key= lambda x:len(x))
    
    if(len(answer) == 0):
        return (len(s))
    
    else:
        return (len(answer[0]))
    