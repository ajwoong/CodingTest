n, k = map(int,input().split())
klist = list(map(int,input().split()))

plug = []

for i in range(k):
    if(len(plug) < n):
        plug.append(klist[i])

    else:
        if(klist[i] not in plug):
            for j in range(i,k):
                if(klist[j] in plug):
                    plug.remove(klist[j])
                    if(plug):
                        plug.pop()
                        plug.append(klist[j])
                    plug.append(klist[i])
    
    print(plug)
                    
