n=int(input())
d=dict()
for _ in range(n):
    s=input()
    if s not in d.keys():
        d[s]=1
    else:
        d[s]+=1

num=max(d.values())
ans=[]
for i in d.keys():
    if d[i]==num:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)