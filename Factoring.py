# factoring.py
def gcf(a, b):
    while b:
        a, b = b, a % b
    return a

def factor_int(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def sign(n):
    return "+" + str(n) if n >= 0 else str(n)

while True:
    print("\n== FACTORING TOOLS ==")
    print("1: GCF (Space Sep)")
    print("2: Factor Integer")
    print("3: Factor Quadratic")
    print("4: Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        raw = input("Nums: ")
        nums = [int(x) for x in raw.split()]
        res = nums[0]
        for n in nums[1:]:
            res = gcf(res, n)
        print("GCF = " + str(res))
    elif choice == "2":
        n = int(input("Integer: "))
        print("Factors: " + str(factor_int(n)))
    elif choice == "3":
        print("ax^2+bx+c")
        a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
        disc = b*b - 4*a*c
        from math import sqrt
        if disc < 0:
            print("Not factorable")
        else:
            sq = sqrt(disc)
            if abs(sq - round(sq)) > 0.0001:
                print("Not factorable")
            else:
                sq = int(round(sq))
                g1 = gcf(abs(-b+sq), 2*a)
                n1, d1 = (-b+sq)//g1, (2*a)//g1
                if d1 < 0: n1, d1 = -n1, -d1
                g2 = gcf(abs(-b-sq), 2*a)
                n2, d2 = (-b-sq)//g2, (2*a)//g2
                if d2 < 0: n2, d2 = -n2, -d2
                print("(" + str(d1) + "x" + sign(-n1) + ")(" + str(d2) + "x" + sign(-n2) + ")")
    elif choice == "4":
        break
      
