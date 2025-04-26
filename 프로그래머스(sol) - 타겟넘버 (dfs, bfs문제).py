# 조금 dfs, bfs 문제에 감이 잡히는거 같다.
# 그래프로 그려서 생각 가능한 문제들은 dfs, bfs로 해결하는게 좋겠다.

numbers = [1, 1, 1, 1, 1]	
target = 3

answer = 0

def dfs(index, result):

    global answer

    if(index == len(numbers)):
        if(result == target):
            answer += 1
        return
    
    else:
        dfs(index + 1, result + numbers[index])
        dfs(index + 1, result - numbers[index])


dfs(0,0)
print(answer)