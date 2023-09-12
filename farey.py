# Naloga privzeta iz: https://github.com/iamvickynguyen/Kattis-Solutions/blob/master/farey.py
#
#==============================================================================

def Euler(n):
    '''Vrne koliko števil je tujih na število n'''
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

phi = [Euler(x) for x in range(3, 10001)] #število tujih števil od 3 do 10000
ans = [0, 0, 3]
for i in range(9998):
    ans.append(ans[-1] + phi[i]) #tabela dolžin Fareq sequenca

p = int(input())
for _ in range(p):
    k, n = map(int, input().split())
    print(k, ans[n])
    
    