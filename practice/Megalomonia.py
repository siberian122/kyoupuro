n = int(input())
task = [list(map(int, input().split())) for _ in range(n)]
task = sorted(task, key=lambda x: x[1])
now = 0
ans = "Yes"
for i in task:
    now += i[0]
    if now > i[1]:
        ans = "No"
        break
print(ans)
