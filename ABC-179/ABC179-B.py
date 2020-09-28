N=int(input())
check=0
Flag=False
for i in range(N):
    d_1,d_2=map(int,input().split())
    if d_1==d_2:
        check+=1
    else:
        check=0
    if check==3:
        Flag=True
if Flag:
    print('Yes')
else:
    print('No')