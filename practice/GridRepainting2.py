
h, w = map(int, input().split())

s = [list(input()) for _ in range(h)]

ans = "Yes"
for i in range(1, h-1):
    for l in range(1, w-1):
        if s[i][l] == "#":
            if s[i+1][l] != "#" and s[i][l+1] != "#" and s[i-1][l] != "#" and s[i][l-1] != "#":
                ans = "No"
                break
print(ans)
