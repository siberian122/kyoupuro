import numpy as np
zone=np.array([[False for _ in range(20)] for _ in range(20) ])
ans=''
for i in range(100):
    x,y=map(int,input().split())
    zone[x][y]=i
    
'''
now=[0,0]
have=[-1]
for i in range(100):
    goal=np.where(zone==i)
    print(goal)
'''