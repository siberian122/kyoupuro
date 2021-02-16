from collections import Counter
import itertools
n = int(input())
l = ["M", "A", "R", "C", "H"]
ans = []
for _ in range(n):
    s = input()
    if s[0] in l:
        ans .append(s[0])
num = 0
S = Counter(ans)
for a, b, c in itertools.combinations(S.keys(), 3):
    num += S[a]*S[b]*S[c]
print(num)
