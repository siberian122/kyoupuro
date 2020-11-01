a,b,c=map(int,input().split())
ans=0
mod=998244353

for i in range(2,a+1):
    for j in range(2,b+1):
        for k in range(2,c+1):
            ans+=i*j*k
print(ans%mod)