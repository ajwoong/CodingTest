# 숫자를 두자리로 출력하고 싶어 앞에 0을 추가하고싶으면 str.zfill(2) 이런식으로하면 두자리수에 공백이 생기면 0을 추가한다
# 처음버스부터해서 최대로 늦게 타는 방법을 업데이트해나가는 방식으로 문제를 해결하였다.

def solution(n, t, m, timetable):
    bus_time = 540
        
    timetable_int = []
    
    for x in timetable:
        hour, minute = x.split(":")
        timetable_int.append(int(hour) * 60 + int(minute))
        
    timetable_int.sort(reverse=True)
    
    cnt = m
    answer = 0
    while(n>0):
        while(cnt!=0 and timetable_int and timetable_int[-1] <= bus_time):
            check = timetable_int.pop()
            cnt -= 1
        
        if(cnt == 0):
            answer = max(answer, check - 1)
        elif(len(timetable_int) == 0):
            answer = max(answer, bus_time)
        else:
            answer = max(answer, bus_time)
        n-=1
        bus_time += t
        cnt = m
    
    
    answer_time =  str(answer//60).zfill(2) + ":" + str((answer%60)).zfill(2)
    return(answer_time)

        
        
            
        
    
    
    
    

        
    