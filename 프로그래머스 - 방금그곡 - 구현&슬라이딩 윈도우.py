# 이번문제는 구현은 까다로웠지만 풀 수 있었다. 구현 과정에서 슬라이딩 윈도우를 이용해 한배열이 다른배열에 속하는지를
# 연산하는 것이 있는데, 이부분을 조금 헷갈렸다. 이 부분을 보완할 수 있도록 해야겠다.

def solution(m, musicinfos):
    
    new_m = []
    for i in range(len(m)):
            if(m[i] == '#'):
                continue
            if(i + 1 < len(m) and m[i+1] == '#'):
                new_m.append(m[i] + m[i+1])
                continue
            new_m.append(m[i])
    
    answer = []
    
    for mi in musicinfos:
        mi_array = mi.split(",")
        
        sh, sm = mi_array[0].split(":")
        fh, fm = mi_array[1].split(":")
        topic = mi_array[2]
        melody = mi_array[3]
        new_melody = []
        
        for mel in range(len(melody)):
            if(melody[mel] == '#'):
                continue
            if(mel + 1 < len(melody) and melody[mel+1] == '#'):
                new_melody.append(melody[mel] + melody[mel+1])
                continue
            new_melody.append(melody[mel])
        
        duration =  int(fh)*60 + int(fm) - (int(sh)*60 + int(sm))
        real_melody = []
        
        for d in range(duration):
            real_melody.append(new_melody[d%len(new_melody)])
        
        n, m = len(real_melody), len(new_m)
        for i in range(n - m + 1):
            if real_melody[i:i + m] == new_m:
                answer.append((duration, topic))
    
    if(not answer):
        return "(None)"
    
    answer.sort(key = lambda x:x[0], reverse=True)
    return answer[0][1]
        