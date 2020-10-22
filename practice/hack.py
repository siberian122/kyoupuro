import itertools
n=int(input())
dictionary=[input() for _ in range(n)]
nn=int(input())
query=[input() for _ in range(nn)]
ans=[]
for i in query:
    i=list(i)
    cnt=0
    for v in itertools.permutations(i,len(i)):
        s=''.join(v)
        #print(s)
        for l in dictionary:
            if l==s:
                cnt+=1
        
    ans.append(cnt) 
print('\n'.join(map(str, ans)))