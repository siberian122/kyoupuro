h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(2**h):
    for j in range(2**w):
        cnt = 0
        for x in range(h):

            if (i >> x) & 1:
                for l in range(w):
                    if (j >> l) & 1:

                        if c[x][l] == "#":
                            cnt += 1
        if cnt == k:
            ans += 1
print(ans)
