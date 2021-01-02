import collections
n = int(input())
d = []
dd = []
for _ in range(n):
    s = input()
    d.append(s)
d = list(set(d))
d = [x if x[0] != '!' else x[1:] for x in d]
ans = "satisfiable"
l = collections.Counter(d)
for k, v in l.items():
    if v > 1:
        ans = k
        break
print(ans)
