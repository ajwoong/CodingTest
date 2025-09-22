# 이 문제는 그리디 문제이다.
# 처음에는 현재 자동차 배치 중에서, 가장 차이가 작게 나는 것들을 제거하는 방식으로 탐욕법을 사용하려 했다.
# 하지만, 그 방법은 사전순 배치 뿐만 아니라 정확한 정답을 보장하지 않았다.

# 그래서, 이후 풀이를 보았다. 풀이는 이진탐색을 통해 1부터 현재 트랙길이 n까지 거리를 늘려나가면서, 어떤 거리가 제일 최대가 될지를
# 계산해서, 거리를 예를들어 5라고했을때 5로 차이나는 경찰차수가 m개 이상이면 그 거리 5부터 또 다시 트랙길이 n까지 이진탐색으로 최대가 되는거리 d를 구하는 방식이다.

# 이후 d를 구했다면, 해당 최대거리 d를 충족하는 경찰차들만 고른후, 답을 추출하면 되는 문제였다.
# 그리디로 구현을 하려 했지만, 처음생각한 그리디 방식은 잘못되었다. 앞으로도 그리디 방식이 잘못되면, 어떻게 다른 방식으로 구현할 수 있을지 생각해봐야겠다.


n, m, k = map(int, input().split())
pos = list(map(int, input().split()))

lo, hi, best = 1, n, 0
while lo <= hi:
    mid = (lo + hi) // 2

    cnt = 1
    last = pos[0]
    for i in range(1, k):
        if pos[i] - last >= mid:
            cnt += 1
            last = pos[i]

    if cnt >= m:      
        best = mid
        lo = mid + 1    
    else:
        hi = mid - 1  

picked = []
for x in pos:
    if not picked or x - picked[-1] >= best:
        picked.append(x)
        last = x
        if len(picked) == m:
            break

answer = ""
for index,value in enumerate(pos):
    if(value in picked):
        answer += "1"
    else:
        answer += "0"

print(answer)



# 첫 풀이
# n ,m ,k = map(int,input().split())
# klist = list(map(int,input().split()))


# for i in range(k-m):
#     diff = []
#     for i in range(len(klist)-1):
#         diff.append(klist[i+1] - klist[i])  
#     min_diff_index = diff.index(min(diff))

#     if(min_diff_index - 1 <0):
#         klist.pop(min_diff_index+1)
#     elif(min_diff_index + 1 >= k-1):
#         klist.pop(min_diff_index)
#     else:
#         if(diff[min_diff_index-1] >= diff[min_diff_index+1]):
#             klist.pop(min_diff_index+1)
#         else:
#             klist.pop(min_diff_index)

# print(klist)