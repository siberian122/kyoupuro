def f(n):
    num=n
    n=n//3
    cnt=0
    for i in range(1,n):
        for l in range(1,n):
            for k in range(1,n):
                if i**2+l**2+k**2+i*l+l*k+k*i==num:
                    cnt+=1
                elif i**2+l**2+k**2+i*l+l*k+k*i>num:
                    break
    return cnt

n=int(input())
for i in range(1,n+1):
    print(f(i))