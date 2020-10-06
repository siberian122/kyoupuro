import math
import itertools
h,w,k=map(int,input().split())

c=[]
ans=0
for i in range(h):
    c.append(list(input().split()))
h=math.factorial(h)
w=math.factorial(w)
for i in range(h):
    p=itertools.permutations(c,i)
    for l in range(len(p)):
        p.count()