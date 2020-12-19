h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
cnt = 101
ans = 0
for ai in a:
    # print(min(ai))
    cnt = min(cnt, min(ai))
    ans += sum(ai)
print(ans-cnt*h*w)
