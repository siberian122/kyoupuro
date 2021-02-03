k, a, b = map(int, input().split())
if b-a < 3:
    # 変えても意味ない
    print(k+1)
else:
    # 回数-交換できるまでの枚数(叩く回数)/2➞お金に変えられる回数
    cnt = (k-(a-1))//2
    if cnt < 0:
        cnt = 0
    if k < a:  # 　叩いても変えられない
        print(k+1)
    ans = a+cnt*(b-a)
    if cnt * 2+a-1 < k:
        ans += 1
    print(ans)
