n,a,b=map(int,input().split())
if abs(a-b)%2==0:
    ans=abs(a-b)//2
else:
    ans=min(a-1,n-b)+1+(b-a-1)//2
print(ans)