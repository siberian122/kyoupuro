def f(n,a):
    num=n
    n=n//3
    cnt=0
    
    for i in range(a,n):
        for l in range(a,n):
            for k in range(a,n):
                if i**2+l**2+k**2+i*l+l*k+k*i==num:
                    cnt+=1
                    fe=min(i,l,k)
                    a=fe
                
    return cnt,a

n=int(input())
a=1
for i in range(1,n+1):
    
    num,a=f(i,a)
    print(num)


    