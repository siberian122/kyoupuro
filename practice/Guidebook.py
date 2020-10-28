import numpy as np
n=int(input())
review=[]
for i in range(n):
    s,p=input().split()
    review.append([i+1,s,int(p)])
review.sort(key=lambda x: (x[1],-x[2]))

for i in review:
    print(i[0])
    
    