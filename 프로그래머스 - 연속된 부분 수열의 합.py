from collections import deque

sequence = [1, 2, 3, 4, 5]		
k = 7

dq = deque()
answer = [0, 1000001]

sum = 0
for x in range(len(sequence)):
    dq.append(x)
    sum += sequence[x]

    while(dq and sum > k):
        a = dq.popleft()
        sum -= sequence[a]
    
    if(sum == k):
        if((dq[-1] - dq[0]) < (answer[-1] - answer[0])):
            answer[0] = dq[0]
            answer[-1] = dq[-1]
        elif((dq[-1] - dq[0]) == (answer[-1] - answer[0])):
            if(dq[0] < answer[0]):
                answer[0] = dq[0]
                answer[-1] = dq[-1]

print(answer)
