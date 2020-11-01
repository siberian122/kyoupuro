n=int(input())
a=list(map(int,input().split()))
l=[0 for _ in range(10**5+1)]
for i in a:
    l[i]+=1
ans=l[0]+l[1]
for i in range(1,10**5-1):
    num=l[i-1]
    num+=l[i]
    num+=l[i+1]
    ans=max(ans,num)
num=l[10**5]
num=+l[10**5-1]
ans=max(ans,num)
print(ans)
    