# dp와 이진탐색(bisect)를 합쳐서 시간복잡도를 더욱 줄이는 문제이다.
# 여기서 헷갈렸던점은 dp에 부분수열을 저장해 나갈때, 나중에 나오는 작은수가 현재 있는 작은수를 대체하는 과정이 이해가 안갔다
# 그러면 나중에 나오는 수가 부분 수열 조건을 깬것이 아닌가 생각했다.
# 그런데 dp 배열은 숫자는 최소로 바꾸려고 하는거고, dp배열의 길이는 증가하는 부분수열의 길이인것은 저장이 되는 것이다.
# 그렇게 숫자는 바뀌어도, 궁극적인 이문제의 정답인 부분수열의 길이정보는 저장되어있고, 이후에 더 작은 것들로 부분수열이 길어지는 순간을 위해
# 업데이트 해주기 위한 방법을 사용한 것이다.

from bisect import bisect_left

n = int(input())
a = list(map(int,input().split()))
dp = []

for i in range(n):
    point = bisect_left(dp, a[i])
    if(point == len(dp)):
        dp.append(a[i])
    else:
        dp[point] = a[i]

print(len(dp))