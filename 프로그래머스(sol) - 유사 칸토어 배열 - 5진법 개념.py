# 5진법을 활용하는것, 0의 위치가 5진법으로 나타냈을때 2를 포함한 숫자이면 0인것을 파악

n = 2
l = 4
r = 17

def is_one(x):
    while(x>=5):
        if((x-2) % 5 == 0):
            return False
        x= x//5
    return x!=2

answer = 0 
for x in range(l-1, r):
    if(is_one(x) == True):
        answer +=1 

print(answer)