n = int(input())
s = input()
r, g, b = s.count("R"), s.count("G"), s.count("B")
cnt = 0
for i in range(n):
    for t in range(1, n//2+1):
        j = i+t
        k = j+t
        if k >= n:
            break
        if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
            cnt += 1
print(r*g*b-cnt)
