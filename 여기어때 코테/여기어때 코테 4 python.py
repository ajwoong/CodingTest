from math import comb

def solution(n):
    binary = format(n, 'b')
    length = len(binary)
    one_count = binary.count("1")
    count = 0

    for i in range(length):
        if(binary[i] == '1'):
            if(length-i-1 >0):
                count += comb(length-i-1, one_count)
            one_count -= 1

    return count

n = int(input())
print(solution(n))