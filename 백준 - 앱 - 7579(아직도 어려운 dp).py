# dp의 점화식이 너무 복잡해서 어렵게 느껴졌다.
# 점화식이 복잡하다는것은 dp의 아이디어가 틀렸다는 것이었다.
# 나는 메모리를 기준으로 dp배열을 만들어 해당 메모리를 만들 수 있는 최소비용을 업데이트 해나가려했다.
# 하지만, 이 문제는 비용을 기준으로 해당 비용으로 만들 수 있는 최대 메모리 크기로 업데이트 해나가는 방식이었다.
# dp의 아이디어를 키우기 위해 더 노력해야겠다.

n, m = map(int, input().split())
m_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

max_cost = sum(c_list) + 1
dp = [0] * max_cost

for i in range(n):
    memory = m_list[i]
    cost = c_list[i]
    for j in range(max_cost-1, cost-1, -1):
        dp[j] = max(dp[j], dp[j-cost] + memory)

for cost in range(max_cost):
    if dp[cost] >= m:
        print(cost)
        break