# quadratics.py
from math import sqrt

def gcf(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_radical(n):
    outside, inside, i = 1, n, 2
    while i * i <= inside:
        while inside % (i*i) == 0:
            outside *= i
            inside //= (i*i)
        i += 1
    return (outside, inside)

def sign(n):
    return "+" + str(n) if n >= 0 else str(n)

while True:
    print("\n== QUADRATIC EQUATIONS ==")
    print("1: Expand (ax+b)(cx+d)")
    print("2: Quadratic Formula")
    print("3: Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        a, b = int(input("a: ")), int(input("b: "))
        c, d = int(input("c: ")), int(input("d: "))
        print(str(a*c) + "x^2 " + sign(a*d+b*c) + "x " + sign(b*d))
    elif choice == "2":
        a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
        disc = b*b - 4*a*c
        if disc < 0:
            print("No real roots")  # See missing items below to upgrade this!
        elif disc == 0:
            print("x = " + str(-b / (2*a)))
        else:
            print("Decimal: x1=" + str(round((-b+sqrt(disc))/(2*a), 3)) + ", x2=" + str(round((-b-sqrt(disc))/(2*a), 3)))
            out, ins = simplify_radical(disc)
            num_gcf = gcf(gcf(abs(b), out), abs(2*a))
            sb, sout, sdenom = -b // num_gcf, out // num_gcf, (2*a) // num_gcf
            mid = "sqrt(" + str(ins) + ")" if sout == 1 else str(sout) + "sqrt(" + str(ins) + ")"
            print("Exact: x = (" + str(sb) + " +/- " + mid + ") / " + str(sdenom) if sdenom != 1 else "Exact: x = " + str(sb) + " +/- " + mid)
    elif choice == "3":
        break
      
