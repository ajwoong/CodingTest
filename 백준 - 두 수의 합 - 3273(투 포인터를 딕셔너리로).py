n = int(input())
alist = list(map(int,input().split()))
x = int(input())
a_dict = {}

for idx, i in enumerate(alist):
    a_dict[i] = (idx, x - i)

count = 0

for i in alist:
    if((a_dict[i][1] in a_dict) and a_dict[i][0] < a_dict[a_dict[i][1]][0]):
        count +=1 

print(count)