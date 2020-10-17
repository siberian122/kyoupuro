x,y,a,b=map(int,input().split())
cnt=0
while (x*a)<(x+b):
    #print(x,cnt)
    if x*a>=y:
        break
    else:
        x*=a
        cnt+=1
cnt+=((y-1)-x)//b
print(cnt)
    

