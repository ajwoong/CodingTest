# 하노이탑을 구현하는 문제이다
# 이러한 문제 유형은 외우는게 좋을 거 같다.
# hanoi(num-1, first, second, third), hanoi(num-1, second, third, first) 는 무슨 말이냐면 입력 n보다 작은 n-1개의 원반을 보조기둥에 옮기고, 그 과정이 끝나면, 보조기둥에 있던걸 다시 목적지 기둥으로 옮기는 과정이다.
# 이유는 n개의 원판을 옮기기 위해서는 n-1개의 원판을 옮기고 n번빼 원판위에 다시 올리는 과정을 거쳐야 하기 때문이다.

answer = []

def hanoi(num, first, third, second):
    global answer
    if(num == 1):
        answer.append([first, third])
        return
    
    hanoi(num-1, first, second, third)
    answer.append([first, third])
    hanoi(num-1, second, third, first)

    
n = int(input())
hanoi(n, 1,3,2)
print(answer)