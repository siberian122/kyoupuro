import itertools
n=input()
ans='No'
l=[i for i in n]
l=list(itertools.permutations(l,3))
#print(l)
for i in l:
    num=''.join(i)
    
    if int(num)%2==0:
        s=int(num)//2
        s=str(s)
        s=s[1:]
        if int(s)%4==0:
            ans='Yes'
print(ans)