from collections import defaultdict

def solution(enroll, referral, seller, amount):
    people = defaultdict(list)
    
    people['-'] = [0]
    for i in enroll :
        people[i] = [0]
    
    
    for i in range(len(referral)):
        if(referral[i] != '-'):
            people[enroll[i]].append(referral[i])
        else:
            people[enroll[i]].append('-')
    
    for i in range(len(seller)):
        now_seller = seller[i]
        now_amount = amount[i] * 100
        while(now_seller != '-' and now_amount != 0 ):
            get_money = now_amount - (now_amount // 10)
            now_amount = now_amount // 10
            people[now_seller][0] += get_money
            now_seller = people[now_seller][1]
        people[now_seller][0] += now_amount
    
    answer = []
    for i in enroll:
        answer.append(people[i][0])
        
    return(answer)