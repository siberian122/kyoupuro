n=int(input())
mod=10**9+7
no_0=9**n
no_9=9**n
no_9_0=8**n
ans=10**n-no_0-no_9+no_9_0
print(ans%mod)
