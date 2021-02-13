n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
ans = 0
for i in range(k):
    now = t[i]
    if now == "r":
        ans += p
    elif now == "s":
        ans += r
    else:
        ans += s
K = t[k-1]
for i in range(k, n):
    now = t[i]

    if now == "r" and K != "r":
        ans += p
        K = now
    elif now == "s" and K != "s":
        ans += r
        K = now
    elif now == "p" and K != "p":
        ans += s
        K = now
    else:
        # k回前と同じなら何出してもいい
        K = "lose"
print(ans)
