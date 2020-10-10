h,w=map(int,input().split())
s=[]
for _ in range(h):
    s.append(list(input()))
#print(s)
cnt=0
#横探索
for i in range(h):
    for l in range(w-1):
        if s[i][l]=='.' and s[i][l+1]=='.':
            cnt+=1
#縦
for l in range(w):
    for i in range(h-1):
        if s[i][l]=='.' and s[i+1][l]=='.':
            cnt+=1
print(cnt)