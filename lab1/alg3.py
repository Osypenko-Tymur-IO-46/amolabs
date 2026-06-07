def calculate(n, b):
    a = 1 
    k = 1 
    t = 1
    z = 0
    while a<=n:
        while k <= a:
            z += pow(a, k) + b/k
            k += 1
        t *= z
        a += 1
        k = 1
        z = 0
    return t 
