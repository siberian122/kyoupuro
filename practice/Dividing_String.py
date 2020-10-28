s=input()
cnt=[0]
n=0
moji=''
for i in s:
    moji+=i
    if cnt!=moji:
        cnt=moji
        moji=''
        n+=1

print(n)