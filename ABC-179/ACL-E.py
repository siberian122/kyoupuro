n,q=map(int,input().split())
s=[0 for _ in range(n)]

for _ in range(q):
    ans=0
    l,r,d=map(int,input().split())
    s[l-1:r]=[d for _ in range(r-l+1)]
    #print(s)
    for i in range(n):
        ans+=s[i]*(10**n-1)
    print(ans%998244353)
