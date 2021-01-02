a, b = input().split()
ans_A, ans_B = 0, 0
for i in a:
    ans_A += int(i)
for i in b:
    ans_B += int(i)
print(max(ans_A, ans_B))
