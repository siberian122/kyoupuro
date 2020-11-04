n=int(input())
k=int(input())
x=list(map(int,input().split()))
ans=0
for i in x:
    if i>=k:
        ans+=2*(i-k)
    elif i>=k-i:
        ans+=2*(k-i)
    else:
        ans+=2*i
print(ans)
        