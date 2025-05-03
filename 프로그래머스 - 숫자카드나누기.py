import math

def solution(arrayA, arrayB):
    
    a_gcd = arrayA[0]
    for i in range(len(arrayA)):
        a_gcd = math.gcd(a_gcd,arrayA[i])
    
    b_gcd = arrayB[0]
    for i in range(len(arrayB)):
        b_gcd = math.gcd(b_gcd, arrayB[i])
    
    b_can_answer = True
    for a in arrayA:
        if(a%b_gcd == 0):
            b_can_answer = False
            break
    
    a_can_answer = True
    for b in arrayB:
        if(b%a_gcd == 0):
            a_can_answer = False
            break
            
    if(a_can_answer == False and b_can_answer == False):
        return 0
    elif(a_can_answer == True and b_can_answer == False):
        return a_gcd
    elif(a_can_answer == False and b_can_answer == True):
        return b_gcd
    else:
        return max(a_gcd,b_gcd)