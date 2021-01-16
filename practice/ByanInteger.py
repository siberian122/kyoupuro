a, b, x = map(int, input().split())
# 二分探索
left = 0
right = 10**9+1
# 条件


def binary(num):
    if (a*num) + (b*len(str(num))) <= x:
        return True


# 実行
ans = 0
while abs(right-left) > 1:
    mid = (left+right)//2
    if binary(mid):
        # 真ん中が条件を満たしていたら➞調べる範囲を右にずらす
        ans = mid
        left = mid
    else:
        # 調べる範囲を小さい数に
        right = mid
print(ans)
