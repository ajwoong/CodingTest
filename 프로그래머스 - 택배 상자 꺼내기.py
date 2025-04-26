n = int(input())
w = int(input())
num = int (input())

height = n // w
left = n % w

answer = []
i = 1

if(left !=0 ): height = height + 1

for x in range(1, height + 1):
    list = []
    for y in range(w):
        if(i>n): list.append(-1)
        else: list.append(i)
        i+=1
    if(x %2 == 0): list.reverse()
    answer.append(list)


index_i = 0
index_j = 0
answer_index_i = 0
answer_index_j = 0

for in_list in answer:
    for x in in_list:
        if(x == num):
            answer_index_i = index_i
            answer_index_j = index_j
            break
        index_j += 1
    index_i +=1
    index_j = 0


answer_num = 1
answer_index_i += 1

while(answer_index_i <= height-1):
    if(answer[answer_index_i][answer_index_j] != -1 ):
        answer_num += 1
    answer_index_i += 1

print(answer_num)