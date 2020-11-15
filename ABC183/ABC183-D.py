import numpy as np
n,w=map(int,input().split())
use=[[0 for i in range(10**9)] for i in range(n)]
for i in range(n):
    s,t,p=map(int,input().split())
    use[n][s:t]=p
L=use.sum(axis=0)
if np.where(use<w):
    print('Yes')
else:
    print('NO')
