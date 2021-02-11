n,m=map(int,input().split())
h=list(map(int,input().split()))
d =dict()

for i in range(m):
    a,b =map(int,input().split())
    if a not in d:
        d[a]=[b]
    else:
        d[a].append(b)
    
    if b not in d:
        d[b] = [a]
    else:
        d[b].append(a)    
cnt = 0
for i in d.keys():
    flag = True
    for j in d[i]:
        if  h[i-1] <= h[j-1]:
            flag = False
            break
    if flag:
        cnt+=1

print(n-len(d)+cnt)