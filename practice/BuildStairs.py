n=int(input())
h=list(map(int,input().split()))
m=h[0]
flag=0
for i in range(1,n):
    if m-h[i]>1:
        flag=1
        break
    else:
        m=max(m,h[i])
print('YNeos'[flag::2])