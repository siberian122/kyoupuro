n, K = map(int, input().split())


def base10_to_n(x, n):
    cnt = x
    out = ""
    while cnt > 0:
        out = str(cnt % n) + out
        cnt = int(cnt/n)
    return str(out)


print(len(base10_to_n(n, K)))
