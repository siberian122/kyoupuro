n,m=map(int,input().split())
sc=[list(map(int,input().split())) for _ in range(m)]
ans=-1
for j in range(10**n):
    j=str(j)
    if len(j)!=n:
        continue
    if all(j[sc[k][0]-1] == str(sc[k][1]) for k in range(m)):
        ans=j
        break

print(ans)