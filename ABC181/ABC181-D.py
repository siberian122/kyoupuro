from collections import Counter
n=input()
ans='No'
if len(n)<=2:
    if int(n)%8==0 or int(n[::-1])%8==0:
        ans='Yes'
    else:
        ans='No'

else:
    cnt=Counter(n)
    for i in range(104,1000,8):
        if not Counter(str(i)) -cnt:
            ans='Yes'     
            break
print(ans) 
