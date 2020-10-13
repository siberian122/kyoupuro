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
if count[0]>0 and count[1]==0:
    print('No')
elif count[1]>0 and count[0]==0:
    print('No')
elif count[2]>0 and count[3]==0:
    print('No')
elif count[3]>0 and count[2]==0:
    print('No')
else:
    print('Yes')