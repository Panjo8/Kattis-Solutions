# 13.vrstica kode iz https://stackoverflow.com/questions/15347174/python-finding-prime-factors
#
#========================================================================================
import sys

def je_prastevilo(n):
    '''Preveri ali je n praštevilo'''
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def find_prime_facs(n):
    '''Razdeli n na praštevilske prafaktorje'''
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def print_output(n, i):
    '''Vrne vrednost po primarni fakorizaciji in
        število ponovitev tega procesa'''
    if je_prastevilo(n): #preverimo če je praštevilo
        print (n, i)
        return 
    i = i + 1 
    factors = sum(find_prime_facs(n)) #razdelimo na praštevila in seštejemo
    print_output(factors, i )
    
[print_output(item, 1) for item in map(int, sys.stdin) if item != 4]

    
    
