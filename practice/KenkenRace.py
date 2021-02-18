n, a, b, c, d = map(int, input().split())
s = input()
# print(s[a:c+1].find("##"))
if s[a:c+1].find("##") != -1 or s[b:d+1].find("##") != -1:
    print("No")
else:
    if c < d:
        print("Yes")
    else:
        if s[b-2:d+1].find("...")==-1:
            print("No")
        else:
            print("Yes")
