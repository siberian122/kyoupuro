n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(n):
    if a[i]<=b[i]:
        ans+=a[i]
        b[i]-=a[i]
        ans+=min(a[i+1],b[i])
        a[i+1]=max(0,a[i+1]-b[i])
    else:
        ans+=b[i]
print(ans)
    