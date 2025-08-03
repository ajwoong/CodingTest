# 한 파티에 참여한 인원, 즉 진실을 미리 알고있는 사람이 해당 파티에서 다른 인원에게 전파하고
# 진실을 나중에 알게 된 사람도, 다른 파티에 참여해서 전파하는 경우를 생각하지 못햇다. 연쇄전파의 방식이엇다.
# 테스트 케이스가 예를들어
# 1 2
# 2 3
# 3 4
# 4 5
# 이렇게 되어있고 5번이 처음부터 진실을 안사람이라면 사실 여부가 모든 파티에 전파되는데 이를 생각하지 못해서
# 변하는게 멈출때 까지 이 truth set을 계속 업데이트 해주면서 길이를 확인해야했다. 
# 그 과정을 구현하기만 하면 문제를 해결할 수 있었다.

from collections import deque

n, m = map(int, input().split())
truth = set(map(int, input().split()[1:]))  

party = []
for _ in range(m):
    party_input = list(map(int, input().split()))[1:]  
    party.append(party_input)

changed = True
while changed:
    changed = False
    for p in party:
        if truth.intersection(p):  
            before = len(truth)
            truth.update(p)
            if len(truth) > before:
                changed = True

count = 0
for p in party:
    if not truth.intersection(p):
        count += 1
        
print(count)