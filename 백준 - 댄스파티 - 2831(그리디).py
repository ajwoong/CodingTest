# 해당 무제는 그리디 문제로 남자, 여자를 음수 양수로 우선 나눈다음, 가장 작은 키를 가진 여자를 한명 씩 비교해가며
# 만약 본인과 키가 같은 사람이 있을때 이를 넘어가고 더 큰 사람을 찾는 방식으로 해결하는 문제였다
# 그리디의 조건을 제대로 확인하면서 해결해야하는 문제다.

from collections import deque

n = int(input())
mlist = list(map(int, input().split()))
wlist = list(map(int, input().split()))

pls_mlist, mns_mlist = [], []
pls_wlist, mns_wlist = [], []

for m in mlist:
    if m > 0:
        pls_mlist.append(m)
    else:
        mns_mlist.append(-m) 

for w in wlist:
    if w > 0:
        pls_wlist.append(w)
    else:
        mns_wlist.append(-w)


pls_mlist.sort()
mns_mlist.sort()
pls_wlist.sort()
mns_wlist.sort()

answer = 0


i, j = 0, 0
while i < len(pls_mlist) and j < len(mns_wlist):
    if pls_mlist[i] < mns_wlist[j]:
        answer += 1
        i += 1
        j += 1
    else:
        j += 1 


i, j = 0, 0
while i < len(mns_mlist) and j < len(pls_wlist):
    if mns_mlist[i] > pls_wlist[j]:
        answer += 1
        i += 1
        j += 1
    else:
        i += 1  

print(answer)