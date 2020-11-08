a,b,c,x,y=map(int,input().split())
ans=a*x+b*y
for i in range(x+y):
    ans=min(ans,i*2*c+max(0,x-i)*a+max(0,y-i)*b)
print(ans)