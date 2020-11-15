import sys
sys.setrecursionlimit(10000000)

mod=10**9+7
s=int(input())
dp=[0 for i in range(s+1)]
dp[0]=1

for i in range(3,s+1):
    dp[i]=(dp[i-1]+dp[i-3])%mod
    #dp<-dp[n]にnの答えが入ってる
    #A[n]=A[n-1]+A[n-3]
#print(dp)
print(dp[-1])