a, b, w = map(int, input().split())
w *= 1000

mina = w // a
maxa = w//b + bool(w % b)
if maxa > mina:
    print("UNSATISFIABLE")
else:
    print(maxa, mina)
