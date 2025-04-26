# 구현이 까다로웠지만 원리는 굉장히 쉬운 문제
# dictionary 정렬을 잘하도록 해야겠고, defaultdict를 더 잘 활용할 수 있도록 해야겠다

from collections import defaultdict

cards = [8,6,3,7,2,5,1,4]

dict = defaultdict(list)
i = 1
for index, card in enumerate(cards):
    p = index
    while(True):
        if(cards[p] != 0):
            dict[i].append(cards[p])
        k = p
        p = cards[p] - 1
        if(cards[k] == 0):
            break
        cards[k] = 0
    i = i+1

sortedDict = defaultdict(list, sorted(dict.items(), key=lambda item: len(item[1]), reverse=True))

if(len(sortedDict) == 1):
    print(0)
else:
    top2 = defaultdict(list, list(sortedDict.items())[:2])
    lengths = [len(v) for v in top2.values()]
    print(lengths[0] * lengths[1])
