n = (input())
N = len(n) % 3
coma = 999
ans = 0
for i in range(1, N + 1):
    ans += (int(n)-int("999" * i))*(i)
print(ans)
# 27182818284590
