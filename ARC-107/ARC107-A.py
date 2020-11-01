a=list(map(int,input().split()))
ans=1
mod=998244353

for i in a:
    ans+=i*(i+1)//2
print(ans%mod)