# 정말 다 풀었는데 break를 걸지 않아서 생긴 실수이다
# 다시는 이런 실수를 하지 않도록 문제를 조심히 읽고 코드를 파악해야겠다

from collections import defaultdict

book_time =  [["09:10", "10:10"], ["09:10", "10:10"], ["10:20", "12:20"], ["10:20", "12:20"]] 

bookTimeNum = []
for x in book_time:
    start = x[0].split(":")
    end = x[1].split(":")
    a = int(start[0]) * 60  + int(start[1])
    b = int(end[0]) * 60 + int(end[1]) + 10
    bookTimeNum.append([a, b])

bookTimeNum.sort()


dict = defaultdict(list)
numberOfRoom = 0
for x in bookTimeNum:
    if(len(dict) == 0):
        numberOfRoom += 1
        dict[numberOfRoom].append(x)

    else:
        check = 0
        for key, value in dict.items():
            if(value[-1][1] <= x[0]):
                check = 1
                dict[key].append(x)
                break
            
        if(check == 0):
            numberOfRoom += 1
            dict[numberOfRoom].append(x)

print(dict)