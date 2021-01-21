s = input()
L = len(s)
ans = [0 for _ in range(L)]
flag, r, l, conv = 0, 0, 0, 0
for i in range(L):
    if s[i] == "R":
        if flag:
            ans[conv:conv+2] = [r//2 + r % 2 + l//2, r//2 + l//2+l % 2]
            flag = 0
            r, l = 0, 0
        r += 1
    else:
        l += 1
        if not flag:
            flag, conv = 1, i-1
ans[conv:conv+2] = [r//2 + r % 2 + l//2, r//2 + l//2+l % 2]
print(*ans)
