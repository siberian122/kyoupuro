from itertools import permutations
import math
n=int(input())
now=list(map(int,input().split()))
elcity=[list(map(int,input().split())) for _ in range(n-1)]
l=[i for i in range(n-1)]
per=permutations(l,n-1)

cost=0
for i in range(n-1):
    num=0
    for l in range(math.factorial(n-1)):

        num+=abs(elcity[per[i]][0]-now[0])+abs(elcity[per[i]][1]-now[1])+max(0,elcity[per[i][2]]-now[2])
        now=elcity[i]
    cost=min(cost,num)
print(cost)

