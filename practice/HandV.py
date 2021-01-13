h, w, k = map(int, input().split())
hw = []
for _ in range(h):
    hw.append(list(input()))

ans = 0
for i in range(2**h):
    for j in range(2**w):

        cnt = 0
        for n in range(h):
            if (i >> n) & 1:

                for m in range(w):
                    if (j >> m) & 1:
                        if hw[n][m] == '#':
                            cnt += 1

        if cnt == k:
            ans += 1

print(hw)
print(ans)
