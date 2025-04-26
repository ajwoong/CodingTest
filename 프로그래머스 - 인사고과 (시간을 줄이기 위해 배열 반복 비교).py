# 이중 포문을 해결하기 위해 정렬을 잘해서 요소별로 비교하고 최대값 저장하는 방식으로 해결함
# 시간복잡도를 계산하고 이를 줄이기 위해서 새로운 방식을 시도하는 것은 성공
# 하지만, 마지막에 등수를 구할때 반복적인 실수로 문제를 조금씩 틀림, + -1 리턴하는 조건도 잘 읽자
# 많이 늘은게 느껴져서 좋았다. -1 리턴하는 조건을 잘 읽도록 하자

def solution(scores):
    wanho = scores[0]
    scores = sorted(scores, key=lambda x:(-x[0], x[1]))
    
    comp = scores[0]
    answer = [scores[0]]
    for i in range(1,len(scores)):
        if(scores[i][0] < comp[0] and scores[i][1] < comp[1]):
            if(wanho == scores[i]):
                return -1
            continue
        else:
            comp = scores[i]
            answer.append(scores[i])
    
    answer = sorted(answer,key=lambda x: sum(x),reverse=True)
    
    cnt = 0
    wanhosum = sum(wanho)
    for i in answer:
        cnt += 1
        if(wanhosum == sum(i)):
            return cnt
    
    