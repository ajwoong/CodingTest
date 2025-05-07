# 이 문제는 이중 for문을 해결하기 위해 dp로 for문 하나를 써서 푸는 문제가 아니였다.
# weight배열은 물론 100,000 까지가 길이기 때문에, 이중 for문을 돌리면 터지지만, weight의 종류가 1000으로 국한되어 있기 때문에
# weight를 counter를 활용해 종류를 잡아주고, 중복을 제거한다음, 쌍에 대한 계산을 for문을 통해 쌍을 이루는것이 있는지와 쌍의 개수가 몇개 나오는지 
# 계산만 해주면 되는 문제였다.
# 시간복잡도를 어떻게 줄일지에 대한 아이디어를 dp로 국한하지 말고, 중복이 있다면 중복을 제거해 종류의 개수로 배열의 크기를 정해주는것도 시간복잡도를 크게 줄일 수 있다는 것을 기억해두자.


from collections import Counter

def solution(weights):
    
    counter = Counter(weights)
    answer = 0
    
    for key, value in counter.items():
        if (value >= 2):
            answer += value*(value-1) // 2
            
    weights = set(weights)
        
    for w in weights:
        if(w*(2/3) in weights):
            answer += counter[w*2/3] * counter[w]
        if (w*(2/4) in weights):
            answer+= counter[w*2/4] * counter[w]
        if (w*(3/4) in weights):
            answer+= counter[w*3/4] * counter[w]
            
    return answer