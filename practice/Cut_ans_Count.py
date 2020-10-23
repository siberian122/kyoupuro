n=int(input())
s=list(input())
ans=0
for i in range(n):
    cnt=0
    mae=s[:i]
    usiro=s[i:]
    for l in mae:
        if l in usiro:
            cnt+=1
            while l in usiro:
                usiro.pop(usiro.index(l))
    ans=max(ans,cnt)
print(ans)
    