from copy import deepcopy

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

wantDict = {}
answer = 0

for x in range(len(want)):
    wantDict[want[x]] = number[x]


i = len(discount) - 10

for k in range(i+1):
    testDict = deepcopy(wantDict)
    zerocount = True
    for p in range(0,10, 1):
        if(discount[k+p] in want):
            testDict[discount[k+p]] -= 1
    for x in testDict.values():
        if(x != 0):
            zerocount = False
    if(zerocount == True):
        answer += 1

print(answer)