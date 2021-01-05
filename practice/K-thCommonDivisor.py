a, b, k = map(int, input().split())


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


la = make_divisors(a)
lb = make_divisors(b)
l = sorted(list(set(la) & set(lb)))
print(l[-k])
