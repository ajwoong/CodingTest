info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


people = []
queryList = []


for x in info:
    xList = x.split()
    people.append(xList)

for x in query:
    x= x.replace(" ", "")
    xList = x.split("and")
    s = xList.pop()
    letters = ''.join([c for c in s if not c.isnumeric()])
    numbers = ''.join([c for c in s if c.isdigit()])
    xList.append(letters)
    xList.append(numbers)
    queryList.append(xList)


searchList = []

for oneQuery in queryList:
    searchNum = 0
    for i in range(len(people)):
        if(((people[i][0] == oneQuery[0]) or oneQuery[0] == '-') and 
           ((people[i][1] == oneQuery[1]) or oneQuery[1] == '-') and
           ((people[i][2] == oneQuery[2]) or oneQuery[2] == '-') and
           ((people[i][3] == oneQuery[3]) or oneQuery[3] == '-') and
           (int(people[i][4]) >= int(oneQuery[4]))):
            searchNum+=1
    searchList.append(searchNum)

print(searchList)