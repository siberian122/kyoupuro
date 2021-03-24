s = input()
past = ""
for i in s:
    if past == i:
        exit(print("Bad"))
    past = i
print("Good")
