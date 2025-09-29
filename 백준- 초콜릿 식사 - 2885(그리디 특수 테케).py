# 2의 제곱형태인 초콜릿은 나눌필요없는 사실을 알아차리지 못했다.
# 항상 모든 테스트 케이스, 특히 특히한 테스트 케이스에대한 사고를 늘려야겠다.

k = int(input())

num = 0
for i in range(21):
    if(2**i > k):
        num = i
        break

if(2**(num-1) == k):
    print(k, 0)

else:
    ksum = 0
    ksum_list = []
    for j in range(num-1, -1, -1):
        if(ksum + 2**(j) <= k):
            ksum += 2**(j)
            ksum_list.append(j)

        if(ksum == k):
            break

    print(2**num, num-ksum_list[-1])