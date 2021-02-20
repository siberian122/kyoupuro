n, k = input().split()


def g1(num):
    return "".join(sorted(num, reverse=True))


def g2(num):
    num = sorted(num)
    return "".join(num)


for i in range(int(k)):
    a = int(g1(str(n)))-int(g2(str(n)))
    n = a
    if n <= 0:
        break
print(a)
