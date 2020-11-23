s, p = map(int, input().split())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


L = make_divisors(p)
ans = 0
for i in range(len(L)-1):
    for l in range(len(L)):
        if L[i]+L[l] == s:
            ans = 1
            break
if ans:
    print('Yes')
else:
    print('No')
