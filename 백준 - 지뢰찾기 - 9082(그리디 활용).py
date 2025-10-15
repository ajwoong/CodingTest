# 그리디를 통한 지뢰찾기 문제이다.
# 해당 문제는, 양끝의 2, 가운데있는 3은 무조건 그 위치에 지뢰가 있어야하므로 그 조건부터 처리한후 문제를 시작한다.
# 그 후에는 맨 왼쪽부터 오른쪽으로 탐색하며 지뢰를 두어도 되는 장소에 배치하면된다. 
# 여기서 지뢰를 두어도 되는 장소란 i-1,i,i+1이 모두 양수이고, #으로 배치가 가능한 장소를 의미한다.

t = int(input())

for test in range(t):
    n = int(input())
    nlist = list(input())
    bomb_list = list(input())

    number_list = []
    for num in nlist:
        number_list.append(int(num))

    for idx, number in enumerate(number_list):
        if(idx == 0 and number == 2):
            bomb_list[idx] = '*'
        elif(idx == n - 1 and number == 2):
            bomb_list[idx] = '*'
        elif(0 < idx < n - 1 and number ==3):
            bomb_list[idx] = '*'

    for idx, bomb in enumerate(bomb_list):
        if(bomb == '*'):
            number_list[idx] -= 1
            if(0 <= idx - 1 <= n - 1):
                number_list[idx-1] -= 1
            if(0<= idx + 1 <= n - 1):
                number_list[idx+1] -= 1
    
    for idx, number in enumerate(number_list):
        if(bomb_list[idx] == '#'):
            if(idx == 0 and number > 0):
                if(number_list[idx + 1] > 0):
                    number_list[idx] -= 1
                    number_list[idx+1] -= 1
                    bomb_list[idx] = '*'
            
            elif(idx == n -1 and number > 0 ):
                if(number_list[idx-1] > 0):
                    number_list[idx] -= 1
                    number_list[idx-1] -= 1
                    bomb_list[idx] = '*'

            elif(0 < idx < n-1 and number > 0):
                if(number_list[idx-1] > 0 and number_list[idx+1] > 0):
                    number_list[idx] -= 1
                    number_list[idx+1] -= 1
                    number_list[idx-1] -= 1
                    bomb_list[idx] = '*'

    answer = 0
    for bomb in bomb_list:
        if(bomb == '*'):
            answer += 1

    print(answer)

    