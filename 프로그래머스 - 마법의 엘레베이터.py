#     1,2,3,4,5 그냥 내려가기 1,2,3,4,5
#     6,7,8,9 -> 올라가서 옆에 1넣기 5,4,3,2
#     2637
#     3 + 2640
#     3 + 4 + 2600
#     3+ 4 + 4+ 3000
#     3+ 4 + 4+ 3
#     십의자리부터 위 규칙대로 실행해서 더하면 답이다!

# 여기서 제일 중요한 포인트는 지금 자리가 5일때의 테세이다. 
# 현재자리가 5일때 다음자리가 5이상이라면, 현재자리에 5를더해서 다음자리를 +1로 만들어주어 0과의 차이를 줄여주어야하고
# 현재자리가 5일때 다음자리가 5미만이라면, 다음자리에 +1을 해주면 오히려 차이가 커지기 때문에 현재자리에서 5를 빼는 방식으로 엘레베이터를 작동해야한다.
# 5에서의 분기 때문에 문제가 발생하는데, 이 부분만 잘 해결하면 쉽게 해결할 수 있다.

def solution(storey):
    
    s_storey = list(str(storey))
    l_s_storey = []

    answer = 0
    for i in s_storey:
        l_s_storey.append(int(i))
    
    l_s_storey.reverse()
    
    while(l_s_storey):
        i = l_s_storey.pop()
        
        if(l_s_storey):
            if(i<5):
                answer += i
            else:
                if(i== 5 and l_s_storey[-1] + 1 < 6):
                    answer += i
                else:
                    answer += 10 - i
                    l_s_storey[-1] += 1
        else:
            if(i<=5):
                answer += i
            else:
                answer += 10 - i + 1
        
    
    return(answer)