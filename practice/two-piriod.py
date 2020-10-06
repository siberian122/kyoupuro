import numpy as np
N,W=map(int,input().split())
w=[]
v=[]
for _ in range(N):
    a,b=map(int,input().split())
    w.append(a)
    v.append(b)

dp=np.zeros(W+1,int)

for i in range(N):
    dp[w[i]:]=np.maximum(dp[:-w[i]]+v[i],dp[w[i]:])

print(dp[-1])
