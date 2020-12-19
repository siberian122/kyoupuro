n = int(input())


def base_to_8(n):
    if (int(n/8)):
        return base_to_8(int(n/8))+str(n % 8)
    return str(n % 8)


ans = 0
for i in range(1, n+1):
    if '7' not in str(i):
        cnt = base_to_8(i)
        if '7' not in str(cnt):
            ans += 1
print(ans)
