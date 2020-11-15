import itertools
import math
n,k=map(int,input().split())
T=[list(map(int,input().split())) for i in range(n)]
L=[i for i in range(2,n+1)]
L=list(itertools.permutations(L))
ans=[]
#print(L)
for i in range(math.factorial(n-1)):
    num=0
    for t in range(n-2):
        next_=L[i][t]-1
        to_=L[i][t+1]-1
        num+=T[next_][to_]
    num+=T[0][L[i][0]-1]+T[L[i][-1]-1][0]
    ans.append(num)
    #print(ans)
print(ans.count(k))
