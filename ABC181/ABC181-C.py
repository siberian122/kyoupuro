#from sympy.geometry import *
import itertools
n=int(input())
r=[i for i in range(n)]
point=[list(map(int,input().split())) for _ in range(n)]
ans='No'
l=list(itertools.combinations(r,3))
for i in l:
    a,b,c=i[0],i[1],i[2]
    x0,y0=point[a][0],point[a][1]
    x1,y1=point[b][0],point[b][1]
    x2,y2=point[c][0],point[c][1]
    if y0*(x1-x2)+y1*(x2-x0)+y2*(x0-x1)==0:
        ans='Yes'
    '''
    AB=((x1-x0)**2+(y1-y0)**2)**0.5
    AC=((x2-x0)**2+(y2-y0)**2)**0.5
    BC=((x2-x1)**2+(y2-y1)**2)**0.5
    if AB+AC==BC or AB+BC==AC or AC+BC==AB:
        ans='Yes'
    '''
print(ans)