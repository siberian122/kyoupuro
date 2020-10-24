a,b,c=map(int,input().split())
ans='NO'
for i in range(a,a*b+1,a):
    if i%b==c:
        ans='YES'
        break
print(ans)