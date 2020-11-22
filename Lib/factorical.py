def factorical(n):#素因数分解
    factor=[]
    i=2
    while n%2==0:
        factor.append(2)
        n//=2
    i=3
    while i*i<=n:
        if n%i==0:
            factor.append(i)
            n//=i
        else:
            i+=2
    if n!=1:
        factor.append(n)
    return factor