s=input()
def chcek(s):
    n=len(s)
    if n%2!=0:
        return False
    elif s[0:n//2]==s[n//2:n]:
        return True
    else:
        return False
while True:
    s=s[0:-1]
    #print(s)
    if chcek(s):
        break
print(len(s))