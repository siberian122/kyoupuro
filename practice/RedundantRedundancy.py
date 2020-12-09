n = int(input())


def gcd(a, b):
    while a > 0:
        a, b = b % a, a
    return b


ans = 1
for i in range(2, n+1):
    ans = ans * i / gcd(ans, i)
print(int(ans+1))
