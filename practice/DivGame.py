from collections import Counter
n=int(input())
def factoricl(n):
    factor=[]
    i=2
    while n%2==0:
        factor.append(2)
        n//=2
    i=3
    while i*i<=n:
        if n%i==0:
            factor.append(i)
            n//=i
        else:
            i+=2
    if n!=1:
        factor.append(n)
    return factor

l=factoricl(n)
l=Counter(l)
ans=0
for i in l.values():
    num=1
    while i>0:
        i-=num
        ans+=1
        num+=1
        if i<0:
            ans-=1
print(ans)

    