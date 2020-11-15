import itertools
n=int(input())
s=input()
ans=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if  str(i) in s:
                argi=s.find(str(i))
                new=s[argi+1:]
                if str(j) in new:
                    argj=new.find(str(j))
                    new=new[argj+1:]
                    if str(k) in new:
                        ans+=1
print(ans)