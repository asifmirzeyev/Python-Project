def toplama(a,b):
    add= a + b
    return add
def cixma(a,b):
    sub= a - b
    return sub
def bolme(a,b):
    division= a / b
    return division
def vurma(a,b):
    mult = a * b
    return mult
def ebob(a,b):
    while b:
        r = a
        a = b
        b = r % b
    return a
def ekob(a,b):
    return a*b/ebob(a,b)
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);


