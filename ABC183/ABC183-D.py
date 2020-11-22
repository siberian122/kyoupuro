import numpy as np
n,w=map(int,input().split())
P=[0 for _ in range(2*10**5+1)]
for _ in range(n):
  s,t,p=map(int,input().split())
  P[s]+=p
  P[t]-=p
P=np.cumsum(P)
#print(P[:10])
if all([i <=w for i in P]):
  print('Yes')
else:
  print('No')