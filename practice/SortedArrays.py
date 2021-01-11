n = int(input())
a = list(map(int, input().split()))
ans = 1
b = ""
up, down = 0, 0
for i in range(n):
    if b == "" and up == 0 and down == 0:
        b = a[i]
    else:
        if a[i] > b:  # 前より大きい時
            if down:  # 変わり目
                up, down = 0, 0
                ans += 1
            else:  # 単調増加し続ける
                up = 1
        elif a[i] < b:  # 前より小さい時
            if up:
                up, down = 0, 0
                ans += 1
            else:
                down = 1
        b = a[i]
print(ans)
