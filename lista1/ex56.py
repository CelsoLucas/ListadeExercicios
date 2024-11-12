def gera_fibonacci(n):
    t1 = 0
    t2 = 1
    c = 2
    while c <= n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        c += 1
    return t3
print(gera_fibonacci(6))