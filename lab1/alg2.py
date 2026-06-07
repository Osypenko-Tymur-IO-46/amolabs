import math

def calculate(k, x):
    if x<=0 or k<=0:
        return "Помилка"
    else: 
        y = k * pow(x, 2) * math.log10(k*x) + math.sqrt(x)
        return y