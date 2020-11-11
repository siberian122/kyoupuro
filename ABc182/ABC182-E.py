from itertools import chain
def main():
    h,w,n,m=map(int,input().split())
    zone=[[0 for i in range(w)]for _ in range(h)]
    light=[[0 for i in range(w)] for _ in range(h)]

    #print(light)
    for i in range(n):
        a,b=map(int,input().split())
        zone[a-1][b-1]=1
    for i in range(m):
        a,b=map(int,input().split())
        zone[a-1][b-1]=2
        
    for i in range(h):
        l=0
        ok=0
        for j in range(w+1):
            if (j==w or zone[i][j]==2):
                if ok:
                    for x in range(l,j):
                        light[i][x]=1
                ok=0
                l=j+1
            if j==w:
                break
            if zone[i][j]==1:
                ok=1
                
    for i in range(w):
        l=0
        ok=0
        for j in range(h+1):
            if (j==h or zone[j][i]==2):
                if ok:
                    for x in range(l,j):
                        light[x][i]=1
                ok=0
                l=j+1
            if j==h:
                break
            if zone[j][i]==1:
                ok=1    
    #print(zone)
    #print(light)
    #print(sum(map(sum,light))) 
    ans=0
    for i in chain.from_iterable(light):
        ans+=1 if i==1 else 0
    print(ans)
 
if __name__=='__main__':
    main()               