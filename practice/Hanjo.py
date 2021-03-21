h, w, a, b = map(int, input().split())
ans = 0


def dfs(i, bit, a, b):
    if i == h*w:
        ans += 1
        return
    if bit
