n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
L=[[]for _ in range(n)]

for i in range(m):
    c,d = map(int,input().split())
    L[min(c,d)-1].append([max(c,d)-1])
kotae='Yes'
for i in range(n):
    ans=0
    cnt=0
    num=[]
    
    for l in range(n+1):
        for k in range(len(L[l])):
            if i==L[l][k]:
                num.append(k)

    for s in num:
        ans+=a[s]
        cnt+=b[s]
    if ans != cnt:
        print(ans,cnt)
        kotae='No'


print(kotae)

    