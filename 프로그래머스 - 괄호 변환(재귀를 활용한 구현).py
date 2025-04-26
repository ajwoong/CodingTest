p = "()))((()"	

pList = list(p)

def isAlright(stringList):
    stack = []
    for char in stringList:
        if(char == '('):
            stack.append(0)
        elif(char == ')'):
            if(stack):
                stack.pop()
            else:
                return False   
    return True


def divide(string):
    if(string == ""):
        return ""
    stringList = list(string)
    stack = []
    left = 0
    right = 0
    check = 0
    u = ""
    v = ""
    for char in stringList:
        if(char == '('):
            u += '('
            left += 1
            stack.append(0)
        elif(char == ')'):
            u += ')'
            right += 1
            if(stack):
                stack.pop()
            else:
                check = 1
        
        if(left == right):
            break
    
    if string.startswith(u):
        v = string[len(u):]
    else:
        v = string

    if(check == 1):
        uList = list(u)
        uList.pop()
        uList.reverse()
        uList.pop()
        uList.reverse()
        newU = ""
        for x in uList:
            if(x=='('):
                newU += ')'
            elif(x==')'):
                newU += '('
        return '(' + divide(v) + ')' + newU
    elif(check == 0):
        return u + divide(v)



if(isAlright(pList) == True):
    print(p)

if(isAlright(pList) == False):
    answer = divide(p)
    print(answer)
