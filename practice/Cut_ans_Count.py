n=int(input())
s=list(input())
ans=0
for i in range(n):
    cnt=0
    mae=s[:i]
    usiro=s[i:]
    ans=max(ans,len(set(mae)&set(usiro)))
print(ans)
    