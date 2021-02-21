n, k = map(int, input().split())


def g1(n):
    return int("".join(sorted(str(n), reversed=True)))


def g2(n):
    return int("".join(sorted(str(n))))


def f(n):
    return g1(n)-g2(n)


for _ in range(k):
    n = f(n)
print(n)
