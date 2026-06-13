import math
 
def function(x):
    return x**3 + 10*x - 9
 
def newton(a, b, e):
    k = 0
    if math.fabs(b - a) < e:
        x = (a + b) / 2
        return x, k
 
    if function(b) * ((function(b + 1e-5) - 2 * function(b) + function(b - 1e-5)) / (1e-5**2)) > 0:
        a, b = b, a
 
    while True:
        x = b - (function(b) / ((function(b + 1e-5) - function(b - 1e-5)) / (2 * 1e-5)))
        k += 1
        if math.fabs(x - b) < e:
            break
        b = x
    return x, k
 
 
def find_intervals(end=10, step=0.5):
    intervals = []
    x = -10
    while x < end:
        if function(x) * function(x + step) < 0:
            intervals.append((x, x + step))
        x += step
    return intervals

