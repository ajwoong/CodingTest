id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

reportArray = [[ 0 for _ in range(len(id_list))] for _ in range(len(id_list))]

for reportRecord in report:
    reportRecordList = reportRecord.split()
    if (reportArray[id_list.index(reportRecordList[0])][id_list.index(reportRecordList[1])] == 0):
        reportArray[id_list.index(reportRecordList[0])][id_list.index(reportRecordList[1])] += 1

print(reportArray)

reportedSum = [0 for _ in range(len(id_list))]

i = 0
for b in range(len(id_list)):
    for a in range (len(id_list)):
        reportedSum[i] += reportArray[a][b]
    i += 1


print(reportedSum)

mailSum = [0 for _ in range(len(id_list))]

p = 0
for x in reportedSum:
    if(reportedSum[p] >= k):
        for y in range(len(id_list)):
            if(reportArray[y][p]>0):
                mailSum[y] += 1
    p += 1

print(mailSum)