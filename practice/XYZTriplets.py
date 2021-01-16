n = int(input())
f = [0 for _ in range(10050)]
for i in range(1, 105):
    for j in range(1, 105):
        for k in range(1, 105):
            num = i*i + j*j + k*k + i*j+j*k+k*i
            if num < 10050:
                f[num] += 1
for i in range(n):
    print(f[i+1])
