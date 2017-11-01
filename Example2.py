from decimal import Decimal 

def fibA(n): 
    fib = [1, 1] 
    if n > 1: 
        for i in range(2, n+1): 
            fib.append(fib[i-2]+fib[i-1])             
    return fib[n] 
    
def golden_ratio(p, dsp = False):
    golden = (1 + Decimal(5 ** 0.5)) / 2 
    goldenP = str(golden)[:(p+2)]
    deviation = (1/(10 ** p))
    FN1 = 0
    FN = 0
    N = 0
    G = 0
    for n in range(1, 61): 
        fn1 = fibA(n+1) 
        fn = fibA(n) 
        g = Decimal(fn1 / fn)
        if dsp:
            print("n=", n, ", fib(", n+1, ")=", \
                  fn1, ", fib(", n, ")=", fn, "golden=", g) 
        if abs(g - Decimal(goldenP)) > 0 \
           and abs(g - Decimal(goldenP)) < Decimal(deviation):
            N = n
            FN1 = fn1
            FN = fn
            G = g
            break
    print("Golden Ratio:", golden)
    print("golden_ratio:", goldenP)
    print("N=", N, ", F(", (N+1), ") / F(", N, ") =", FN1, "/", FN)
    print("golden_ratio(", p, ")=", G)

