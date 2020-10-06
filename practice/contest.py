d=int(input())
c=list(map(int,input().split()))
c_days=[0]*26
c_days_2=[0]*26
fir_ans=0
sec_ans=0
for i in range(d):
    s=list(map(int,input().split()))
    #最大満足度を選択
    n=s.index(max(s))
    c_days_2[n]=i+1
    if i==0:
        nn=s.index(max(s))
    else:
        #最大不満を回避
        c_low=[c[x]*(i+1-c_days[x]) for x in range(26)]
        #print(*c_low)
        nn=c_low.index(max(c_low))
        sec_ans+=s[nn]
        c_days[nn]=i+1

    los_1=[c[x]*(i+1-c_days_2[x]) for x in range(26)]
    los_2=[c[x]*(i+1-c_days[x]) for x in range(26)]
    fir_ans-=sum(los_1)
    sec_ans-=sum(los_2)
    if fir_ans>=sec_ans:
        print(n+1)
        sec_ans=fir_ans
        c_days=c_days_2
    else:
        print(nn+1)
        fir_ans=sec_ans
        c_days_2=c_days
print(sec_ans)