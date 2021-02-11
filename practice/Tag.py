a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if v <= w:
    print("NO")
else:
    if abs(a-b) <= (v-w)*t:
        print("YES")
    else:
        print("NO")
