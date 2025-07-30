# 이 문제는 투 포인터를 활용한 문제였다.
# 투 포인터 문제는 모든 종류의 보석을 일단 포함할때까지 윈도우를 오른쪽으로 +1 씩 계속 늘리다가
# 모든 종류의 보석을 포함했다면 이후부터 왼쪽을 +1씩 늘려서 윈도우 사이즈를 줄여가는 것이었다.
# 이 과정을 반복해 최소의 슬라이딩 윈도우 크기를 찾아내는 문제였다.
# 슬라이딩 윈도우 문제가 자주 나오니 이런건 제발 잘 풀자.

from collections import defaultdict
import math

def solution(gems):
    gems_set = set(gems)
    kinds = len(gems_set)
    gem_dict = defaultdict(int)

    left = 0
    right = 0
    now_kind = 0
    min_len = math.inf
    answer = [0, 0]

    while right < len(gems):
        
        if (gem_dict[gems[right]] == 0):
            now_kind += 1
        gem_dict[gems[right]] += 1
        right += 1
        
        while (now_kind == kinds):
            if right - left < min_len:
                min_len = right - left
                answer = [left + 1, right]  

            gem_dict[gems[left]] -= 1
            if (gem_dict[gems[left]] == 0):
                now_kind -= 1
            left += 1

    return answer