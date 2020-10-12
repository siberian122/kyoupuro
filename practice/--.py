s=list(input())
a=[0 for i in range(len(s)+1)]
ans=0
for i in range(len(s)):
    if s[i]=='<':
        a[i+1]=max(a[i]+1,a[i+1])
for i in range(len(s)-1,-1,-1):
    if s[i]=='>':
        a[i]=max(a[i],a[i+1]+1)
print(sum(a))
    