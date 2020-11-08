n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
ans=0
for i in range(2*n):
    if i%2:
        ans+=a[i]
print(ans)