
c=list(map(int,input().split()))
c.sort()
Flag=False
eat=c[0]+c[-1]
have=c[1]+c[-2]
if eat==have:
    Flag=True
eat=c[0]+c[1]+c[2]
if eat == c[-1]:
    Flag=True
    
if Flag:
    print('Yes')
else:
    print('No')
