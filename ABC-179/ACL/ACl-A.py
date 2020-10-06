a,b,c,d=map(int,input().split())
Flag=False
if a<=c:
    if c<=b:
        Flag=True
else:
    if d>=a:
        Flag=True
if Flag:
    print('Yes')
else:
    print('No')