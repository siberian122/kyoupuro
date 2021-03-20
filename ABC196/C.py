n = input()
ans = 0
x = len(n)
cnt = 1

for i in range(1, 12, 2):
    if x > i:

        if x == 2:  # 桁が偶数の時
            ans += int(n[0])-1
            ans += bool(int(n[0]) <= int(n[1]))
        elif x == i+1:
            ans += int(n[:x//2])-10**(x//2-1)
            ans += bool(int(n[:x//2]) <= int(n[x//2:]))
        else:
            ans += 10**(i-cnt)*9
            # print(ans)

    cnt += 1
print(ans)
