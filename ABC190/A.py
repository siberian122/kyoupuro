a, b, c = map(int, input().split())
if a > b:
    print("Takahashi")
elif b > a:
    print("Aoki")
else:
    if c == 0:
        print("Aoki")
    else:
        print("Takahashi")
