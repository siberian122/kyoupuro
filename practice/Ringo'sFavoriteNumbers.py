d,n=map(int,input().split())
if n<=99:
    Na=n*(100**d)
elif n==100:
    Na=101*(100**d)
print(Na)