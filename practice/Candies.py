n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(n):
    num=sum(a[:i+1])
    #print(a[:i+1],b[i:])
    num+=sum(b[i:])
    ans=max(num,ans)
print(ans)
    