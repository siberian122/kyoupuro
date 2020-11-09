n=int(input())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors
ans=10**12+10**12
for i in make_divisors(n):
    num=i-1+n//i-1
    
    ans=min(ans,num)
print(ans)