s = input()
for i in range(len(s)):
    # print(i)
    if i % 2:
        if s[i].islower():
            exit(print("No"))
    else:
        if s[i].isupper():
            exit(print("No"))
print("Yes")
