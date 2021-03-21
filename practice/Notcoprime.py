from math import gcd
n = int(input())
X = list(map(int, input().split()))
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ans = float("inf")
for i in range(1, 1 << 15):  # 2**15通り
    a = 1
    for j in range(15):  # 15この素数をかけるかけないか
        if i & (1 << j):
            a *= p[j]
    if all(gcd(x, a) > 1 for x in X):
        # できた数が　x　と素になっているか
        ans = min(ans, a)
print(ans)
