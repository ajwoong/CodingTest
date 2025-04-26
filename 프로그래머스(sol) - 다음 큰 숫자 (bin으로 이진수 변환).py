# bin은 어떤 자연수를 이진수로 변화하는 함수이다
# string으로 값이 나오기 때문에 '0b101110..' 이런식으로 값이 나올 것이다
# 그래서 count를 통해 1 또는 0의 개수를 세줄 수 있다. 앞으로 이 방식을 제대로 활용하자
# 너무 쉬운 문제임에도 틀렸다. 분발하자

def solution(n):
    
    twoCount = bin(n).count("1")
    
    while True:
        n += 1
        if(bin(n).count("1") == twoCount):
            return n