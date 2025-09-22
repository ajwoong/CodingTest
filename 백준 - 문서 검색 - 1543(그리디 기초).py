doc = input()
target = input()
answer = 0

while(doc.find(target) != -1):
    target_index = doc.find(target)
    answer += 1
    doc = doc[target_index + len(target) : ]


print(answer)