n=int(input())
c = input()
l=[0 for _ in range(n)]
ans=0
for i in range(n):
    if c[i] == "R":
        ans+=1
    l[i] = ans
print(ans-l[ans-1])
