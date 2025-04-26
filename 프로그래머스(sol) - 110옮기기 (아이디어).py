# 이 문제는 아이디어가 중요한 문제였다.
# 발견할 수 있는 110들을 전부 pop하고 가장 마지막 0 다음자리에 110을 넣었을때가 항상 사전순으로 앞서는, 즉 최소값을 만드는 방법이다.
# 이 아이디어를 나는 선행하는 111뒤에 110이 있으면 110이 111앞으로 들어가야한다고 파악햇다.
# 이유는 110은 111보다 항상 작기 때문에, 111이 있다면 그 자리와 바뀌어야한다고 생각했다.
# 하지만 이건 0 다음자리에 무조건 110을 넣는 문제이다. 그 이유는 110은 어짜피 넣어야하고, 어짜피 넣을 경우
# 사전순으로 가장 앞서게 만들기 위해서는 0을 최대한 앞에다 넣고 가장 마지막 0이 있는경우에 그 위치 다음으로 110을 삽입해야 하기 때문이다. 


def solution(s):
    
    result = []

    for i in s:
        temp = []
        count_110 = 0

        for ch in i:
            temp.append(ch)
            if len(temp) >= 3 and temp[-3:] == ['1', '1', '0']:
                temp.pop()
                temp.pop()
                temp.pop()
                count_110 += 1

        idx = -1
        for j in range(len(temp)):
            if temp[j] == '0':
                idx = j

        
        insert_pos = idx + 1
        answer = temp[:insert_pos] + ['110'] * count_110 + temp[insert_pos:]
        result.append(''.join(answer))

    return result