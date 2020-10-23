a,b,c=map(int,input().split())
Flag=False
for i in range(101):
    num=(i*b+c)/a
    
    if num.is_integer():
        Flag=True
        break
if Flag:
    print('Yes')
else:
    print('No')