r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
ans=4
if r1==r2 and c1==c2:
    exit(print(0))
for i in range(-3,4):
    l=abs(i)-3
    if r1+i+c1+l==r2+c2 or (r1+i)-(c1+l)==r2-c2 or abs(r1+i-r2)+abs(c1+l-c2)<=3:
        if i==0 and l==0:
            ans=1
            break
        else:
            ans=2
    
if r1+c1==r2+c2 or r1-c1==r2-c2 or abs(r1-r2)+abs(c1-c2)<=3:
    ans=1

elif (r1+c1)%2==(r2+c2)%2:
    ans=2
 
else:
    ans=min(ans,3)
print(ans)    