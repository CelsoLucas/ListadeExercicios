def aproxima_pi(n):
    pi_aproximado = 0
    for i in range(n):
        termo = (-1) ** i / (2 * i + 1) 
        pi_aproximado += termo
    pi_aproximado *= 4 
    return pi_aproximado
n = 1000  
print(aproxima_pi(n)) 

