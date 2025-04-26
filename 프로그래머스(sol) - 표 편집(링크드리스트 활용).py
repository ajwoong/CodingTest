# 처음 링크드 리스트 없이, string으로 구현을 하고, string을 문자열 슬라이싱해서 풀려고 했다.
# 정확성 테스트는 전부 맞았지만, 효율성테스트를 하나도 못 맞았다.
# 이유가 뭘까 하고 봤는데, string을 슬라이싱 할때 O(n)의 시간복잡도가 든다.
# 그래서 링크드리스트로 해당 인덱스의 이전 인덱스 (prev)와 다음 인덱스 뭔지를 저장하는 리스트 (next) 를 만들어서 이걸로 해결하는것이 시간복잡도를 O(1) 까지로 줄일 수 있는 방법이었다.
# 링크드 리스트를 직접 구현해서 푸는 문제는 처음이었다. 이런 문제가 나오면 슬라이싱에 드는 시간을 구하고 시간복잡도를 파악한 후
# 링크드 리스트가 더효율적인지 잘 살펴 보아야겠다.


# 문자열 슬라이싱으로 푼 내 풀이
def solution_with_string_slicing(n, k, cmd):
    
    s = ""
    for i in range(n):
        s = s + chr(i+65)
    
    dlist = []
    for c in cmd:
        clist = c.split(" ")
        if(clist[0] == "D"):
            k += int(clist[1])
        elif(clist[0] == "U"):
            k -= int(clist[1])
        elif(clist[0] == "C"):
            dlist.append([k,s[k:k+1]])
            s = s[:k] + s[k+1:]
            if(k == len(s)):
                k -= 1
        elif(clist[0] == "Z"):
            p = dlist.pop()
            s= (s[:p[0]] + p[1] + s[p[0]:])
            if(p[0] <= k):
                k+=1
                
    s = set(s)            
    
    answer = ""
    for i in range(n):
        if(chr(i+65) in s):
            answer = answer + "O"
        else:
            answer = answer + "X"
    
    return(answer)

        

def solution_with_linked_list(n, k, cmd):
    
    prev = [i - 1 for i in range(n)]
    nxt = [i + 1 for i in range(n)]
    nxt[-1] = -1  

    dlist = []
    removed = [False] * n

    for c in cmd:
        clist = c.split(" ")
        if clist[0] == "D":
            x = int(clist[1])
            for _ in range(x):
                k = nxt[k]
        elif clist[0] == "U":
            x = int(clist[1])
            for _ in range(x):
                k = prev[k]
        elif clist[0] == "C":
            dlist.append((k, prev[k], nxt[k]))
            removed[k] = True
            if prev[k] != -1:
                nxt[prev[k]] = nxt[k]    
            if nxt[k] != -1:
                prev[nxt[k]] = prev[k]
            
            if nxt[k] != -1:
                k = nxt[k]
            else:
                k = prev[k]
                
        elif clist[0] == "Z":
            p = dlist.pop()
            removed[p[0]] = False
            if p[1] != -1:
                nxt[p[1]] = p[0]
            if p[2] != -1:
                prev[p[2]] = p[0]
                
                
    answer = ""
    for i in range(n):
        if(removed[i]):
            answer += "X"
        else:
            answer += "O"
        
    return answer            