# dfs와 백트래킹을 함께 섞은 문제였다
# 이 문제에서는 dfs로 경로 탐색을 하되, 더이상 진행할 수 없는 경로가 있다면 끝으로 빼주기, 즉 그 경로를 저장하고
# 다른 경로로 갈 수 있도록 해야한다
# 그래서 나는 dfs 까지 구현은 하였지만 백트래킹 구현이 어려웠다
# 백트래킹 구현은 경로를 진행하다가 dictionary에서 더이상 뻗어날 곳이 없으면 answer list에 append 해서
# 끝난 경로를 추가해 현재까지의 경로를 저장하는 방식으로 구현을 하였다. 그러면 answer list를 역순으로 정렬한것이
# 여행지 경로가 될것이다. dfs 구현까지는 직접 하고 생각으로도 실천해냈지만 백트래킹으로 현재까지 경로 저장이 매우 어려운 것 같다.
# 백트래킹의 감이 조금 잡히는게, 항상 현재까지의 경로를 정답 list에 다 pop해서 저장하고, 그 이후에 다시 경로를 진행해서 그 경로도 저장하고
# 즉, 경로 여러개를 저장하는 방식으로 구현하는게 백트래킹 같다. 백트래킹의 방식과 속성을 잘 공부하자!!!!


from collections import defaultdict

def solution(tickets):
    
    dict_tickets = defaultdict(list)
    
    for t in tickets:
        dict_tickets[t[0]].append(t[1])
    
    for key,value in dict_tickets.items():
        value.sort(reverse=True)
    
    
    stack = []
    stack.append("ICN")
    
    answer = []
                
    while stack:
        while dict_tickets[stack[-1]]:
            stack.append(dict_tickets[stack[-1]].pop())
        answer.append(stack.pop())
    
    answer.reverse()
    return(answer)
    
