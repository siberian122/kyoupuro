A = list(input())
B = list(input())
C = list(input())
a, b, c = 1, 0, 0
na = len(A)
nb = len(B)
nc = len(C)


now = A[0]
while True:

    if now == "a":
        if na == a:
            exit(print("A"))
        now = A[a]
        a += 1
    elif now == "b":
        if nb == b:
            exit(print("B"))
        now = B[b]
        b += 1
    else:
        if nc == c:
            exit(print("C"))
        now = C[c]
        c += 1

    print(a, b, c, now)
