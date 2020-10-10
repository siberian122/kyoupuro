s=list(input())
count=[0 for i in range(4)]
for i in s:
    if i=='N':
        count[0]+=1
    elif i=='S':
        count[1]+=1
    elif i=='E':
        count[2]+=1
    elif i=='W':
        count[3]+=1
