n = int(input())
a = list(map(int, input().split()))
mae = []
ushiro = []
N = n % 2
for i in range(n):
    if i % 2 != N:
        mae.append(a[i])
    else:
        ushiro.append(a[i])
    # print(mae+ushiro)
print(*mae[::-1]+ushiro)
