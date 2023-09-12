#  4. vrstica je narejena s pomočjo: https://stackoverflow.com/questions/18114138/computing-eulers-totient-function
# 11. vrstica je narejena s pomočjo: https://stackoverflow.com/questions/15347174/python-finding-prime-factors
#==========================================================================================================
def Euler(n):
    prastevila = prastevila_faktorji(n)
    rez = n
    for i in prastevila:
        rez *= (1-1/i)
    return int(rez)

def prastevila_faktorji(n):
    '''Vrne množico praštevil, ki delijo število n'''
    prastevila = set() 
    while not n % 2:
        prastevila.add(2)
        n //= 2
    i = 3
    while i * i <= n:
        while not n % i:
            prastevila.add(i)
            n //= i
        i += 2
    if n != 1:
        prastevila.add(n)
    return prastevila

n = int(input())
while n != 0:
    print(Euler(n))
    n = int(input())
    



    