n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
if n >= m:
    print(0)
else:
    x = sorted([x[l+1]-x[l]for l in range(m-1)])
    # 動かなきゃいけないスペースの小さいほうのコマ数分
    print(sum(x[:m-n]))
