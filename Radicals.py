# radicals.py
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

while True:
    print("\n== RADICAL TOOLS ==")
    print("1: Simplify sqrt(n)")
    print("2: Simplify sqrt(a/b)")
    print("3: Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        n = int(input("n = "))
        out, ins = simplify_radical(n)
        print("= " + (str(out) if ins == 1 else "sqrt(" + str(ins) + ")" if out == 1 else str(out) + "sqrt(" + str(ins) + ")"))
    elif choice == "2":
        a, b = int(input("a: ")), int(input("b: "))
        g = gcf(a, b); a //= g; b //= g
        on, in_ = simplify_radical(a)
        od, id_ = simplify_radical(b)
        oc, ic = simplify_radical(in_ * id_)
        fn, fd = on*oc, od*id_
        g2 = gcf(fn, fd); fn //= g2; fd //= g2
        print("Decimal: " + str(round(sqrt(a/b), 4)))
        print("Exact: " + (str(fn) if ic == 1 else str(fn) + "sqrt(" + str(ic) + ")") + ("" if fd == 1 else "/" + str(fd)))
    elif choice == "3":
        break
      
