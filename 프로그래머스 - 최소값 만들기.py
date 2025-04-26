A = [1, 4, 2]	
B = [5, 4, 4]

A.sort()
B.sort()
B.reverse()

answer = 0
for x in range(len(A)):
    answer += A[x] * B[x]

print(answer)