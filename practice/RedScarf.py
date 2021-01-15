n = int(input())
a = list(map(int, input().split()))
all_xor = 0
for i in a:
    all_xor ^= i
ans = []
for i in a:
    ans.append(all_xor ^ i)
print(*ans)
