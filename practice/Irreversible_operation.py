s=input()
cnt=0
ans=0
for i in s:
    if i=='B':
        cnt+=1
    else:
        ans+=cnt
print(ans)