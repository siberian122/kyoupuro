h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans=0
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if min(k,l)>=0 and k<h and l<w and s[k][l]=='#':
                    ans+=1
        if s[i][j]=='.':
            s[i][j]=ans
for i in range(h):
    for j in range(w):
        print(s[i][j],end='')
    print()