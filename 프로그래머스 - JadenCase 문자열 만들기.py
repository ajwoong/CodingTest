s = "3people unFollowed me"	

s.lower()
sList = s.split(" ")

answer = ""
for index, x in enumerate(sList):
    k = x.capitalize()
    if(index == 0):
        answer += k
    else:
        answer = answer + " " + k
    
print(answer)